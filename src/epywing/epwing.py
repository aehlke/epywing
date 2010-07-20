# -*- coding: utf-8 -*-

from eb import *
import sys
from os import path
import string
from lxml import html
from lxml.cssselect import CSSSelector

from mybase64 import urlsafe_b64_encode, urlsafe_b64_decode, _num_decode, _position_to_resource_id, _ENTRY_ID_SPLIT
from uris import EpwingUriDispatcher
from gaiji import GaijiHandler
import util
import struct
from titles import BookTitle
from epwingentry import Entry

#TODO refactor hooks - DRY

#EB API reference http://www.sra.co.jp/people/m-kasahr/eb/doc/eb-09.html


         

class Container(object):
    '''To share state in Epwing parser callbacks.
    '''

    # This is used for an unfortunate yet necessary hack,
    # for determining where entries end.
    EARLY_ENTRY_TERMINATOR = '__MANABI_EARLY_ENTRY_TERMINATOR__'

    def __init__(self, debug_mode=False):
        self.debug_mode = debug_mode
        self.reference_stack = []
        self.decoration_stack = None
        self.first_indent_level = None
        self.indent_stop_code_count = 0
        self.read_count = 0
        self.indent_stop_code_in_first_read = False
        self.buffer = u''


class EpwingBook(object):

    def __init__(self, book_path, subbook=None, gaiji_handler=None, manager=None):
        '''`gaiji_handler` is a handler class, not an instance.
        `subbook` is the index of the subbook within this EPWING book that this EpwingBook instance will represent.
        If it is None, then it will default to representing all available subbooks, instead of a single one.
        '''
        self.book_path = book_path #TODO verify path is valid
        self.subbook = subbook
        self._subbook = None
        self.gaiji_handler = gaiji_handler(self) if gaiji_handler else GaijiHandler(self)

        self.manager = manager

        self.id = path.basename(self.book_path)
        if subbook is not None:
            self.id += ':{0}'.format(subbook)
        self.id = urlsafe_b64_encode(self.id)

        self.uri_dispatcher = EpwingUriDispatcher(self)
        self.book, self.appendix, self.hookset = EB_Book(), EB_Appendix(), EB_Hookset()

        try:
            eb_bind(self.book, self.book_path.encode('utf-8'))
        except EBError, (error, message):
            code = eb_error_string(error)
            raise Exception('Error: %s: %s\n' % (code, message))

        if self.subbook is None:
            self.name = path.basename(self.book_path)
        else:
            self.name = eb_subbook_title2(self.book, int(self.subbook)).decode('euc-jp')

        # Get the corresponding BookTitle subclass instance
        # (may be None if unknown)
        self.title = BookTitle.get_title(self)


    #def __enter__(self):_html_escape_left
    #    eb_initialize_library()
    #    return self
    
    #def __exit__(self, type, value, traceback):
    #    eb_finalize_library()


    @property
    def _search_methods(self):
        '''Returns the search methods this dictionary supports, plus the corresponding EB method.
        [('name', meth,),]
        '''
        all_methods = {'exact': (eb_have_exactword_search, eb_search_exactword,),
                       'prefix': (eb_have_word_search, eb_search_word,),
                       'suffix': (eb_have_endword_search, eb_search_endword,),
                       'keyword': (eb_have_keyword_search, eb_search_keyword,),
                       #'multi': (eb_have_multi_search, eb_search_multi,),
        }

        subbook = int(self.subbook) if self.subbook else 0
        self._set_subbook(subbook)

        return dict((key, val[1],) for key, val in all_methods.items() if val[0](self.book))

    @property
    def search_methods(self):
        '''Returns a list of the search methods that this dictionary file supports.
        '''
        return self._search_methods.keys()

    #TODO separate URI from ID - have both!?

    def _set_subbook(self, subbook):
        subbook = int(subbook)
        if self._subbook != subbook:
            eb_set_subbook(self.book, subbook)
            self._subbook = subbook

    @property
    def subbooks(self):
        '''Returns a list of the subbooks, with their name, URI and directory, for the current book
        '''
        #TODO make this into a property only if self.subbook is None
        ret = []
        for subbook in eb_subbook_list(self.book):
            id = str(subbook)
            ret.append({ 'name': eb_subbook_title2(self.book, subbook).decode('euc-jp'),
                         'directory': eb_subbook_directory2(self.book, subbook),
                         'id': id,
                         #'uri': self.uri_dispatcher.uri('subbook', subbook=id)
            })
        return ret

    #TODO test this
    def audio(self, audio_id, subbook_id):
        self._set_subbook(subbook_id)
        page, offset, data_size = map(_num_decode, audio_id.split(_ENTRY_ID_SPLIT))
        end_page = page + (data_size / EB_SIZE_PAGE)
        end_offset = offset + (data_size % EB_SIZE_PAGE)
        if EB_SIZE_PAGE <= end_offset:
            end_offset -= EB_SIZE_PAGE
            end_page += 1

        #read sound data
        eb_set_binary_wave(self.book, (page, offset,), (end_page, end_offset,))
        wave_data = eb_read_binary(self.book)

        #if there are extra data (32 bytes) before fmt chunk, remove them
        if wave_data[44:48] == 'fmt ' and wave_data[12:16] != 'fmt ':
            wave_data = wave_data[:12] + wave_data[44:]
        return wave_data

    def search(self, query, subbook=None, search_method='exact', search_options=None):
        '''Searches this book and yields matching entries.
        Only set `subbook` if `self.subbook` is None (though it is not necessary - all subbooks will be 
        searched if both are None).
        '''
        if not query:
            return
        if not self.subbook and not subbook:
            #search all subbooks of this book
            for subbook in self.subbooks:
                for result in self.search(query, subbook=subbook['id'], search_method=search_method, search_options=search_options):
                    yield result
            return
        else:
            subbook = int(self.subbook)

        self._set_subbook(subbook)
        encoded_query = query.encode('euc-jp')
        if not encoded_query.strip():
            return
        try:
            self._search_methods[search_method](self.book, encoded_query)
        except EBError:
            return

        # Sometimes multiple headings in a search results hit list point
        # to the same text location. We'll keep track of these text locations
        # so that we don't add duplicate hits.
        text_location_hits = []

        while True:
            hits = eb_hit_list(self.book)
            if not hits:
                break
            for heading_location, text_location in hits:
                if text_location not in text_location_hits:
                    text_location_hits.append(text_location)
                    entry = Entry(self, subbook, heading_location, text_location)
                    yield entry

    def _get_content(self, *args, **kwargs):
        return u''.join([e for e in self._get_content_iterator(*args, **kwargs)])

    def _get_content_iterator(self, subbook, position, container, content_method):
        def clean_data(data):
            data = unicode(data, 'euc-jp', errors='ignore')

            # handle HTML escaping, since we add HTML tags, but entries may contain < and > characters
            data = data.replace('<', '&lt;')
            data = data.replace('>', '&gt;')
            data = self._unescape_html(data)

            data = self.gaiji_handler.replace_all_gaiji_tags(data)

            if content_method != eb_read_heading:
                data = self._fix_html_hacks(data)
                data = self._fix_anchor_links(data)
            return data

        container = Container()#debug_mode=True)
        self._set_subbook(subbook)
        self._set_hooks(content_method)
        self._buffer_entry_count = 0
        self._buffer_start_position = position
        data = ''
        eb_seek_text(self.book, position)

        for i in xrange(400): # this value just has to be sufficiently large to cover the longest entries
            buffer_ = []

            while True:
                try:
                    data_chunk = content_method(self.book, self.appendix, self.hookset, container)
                except EBError, e:
                    break

                if not data_chunk:
                    break

                buffer_.append(data_chunk)

            container.read_count += 1

            if container.read_count == 1 and container.indent_stop_code_count >= 1:
                container.indent_stop_code_in_first_read = True

            data += ''.join(buffer_)

            if container.debug_mode:
                data += '[--eor--]'

            i = data.find(container.EARLY_ENTRY_TERMINATOR)
            if i != -1:
                data = data[:i]
                break

            if content_method == eb_read_heading:
                break

            #FIXME sometimes goes too far now
            try:
                pos = eb_forward_text(self.book, self.appendix)
            except EBError, (error, message):
                break

            yield clean_data(data)
            data = ''

        if data:
            yield clean_data(data)
    
    def _fix_anchor_links(self, text):
        '''If a reference links to a position within the entries already loaded,
        then its link will be rewritten to point to the named anchor.
        '''
        doc = html.fromstring(text)
        anchor_names = [anchor.attrib['name'] for anchor in doc.cssselect('a[name]')]
        for reference in doc.cssselect('a[href]'):
            if reference.attrib['href'] in anchor_names:
                reference.attrib['href'] = '#' + reference.attrib['href']
            else:
                reference.attrib['href'] = self.uri_dispatcher.uri_base + reference.attrib['href']
        return html.tostring(doc)

    def _fix_html_hacks(self, text):
        text = u'<div>{0}</div>'.format(text)
        doc = html.fromstring(text)
        
        # rewrite attributes
        for hack_tag in doc.cssselect('hack_attribs'):
            prev_tag = hack_tag.getprevious()
            attribs = dict((key, val) for key, val in hack_tag.attrib.items())
            prev_tag.attrib.update(attribs)
            hack_tag.drop_tag()
        
        # fix indentation divs
        hack_divs = doc.cssselect('hack_indent')
        to_drop = []
        for hack_div in hack_divs:
            indent_div = html.Element('div')
            attribs = dict((key, val) for key, val in hack_div.attrib.items())
            indent_div.attrib.update(attribs)
            hack_div.addnext(indent_div)
            hack_div.drop_tag()
            indent_div.text = indent_div.tail
            indent_div.tail = ''
        
            for sibling in indent_div.itersiblings():
                if sibling.tag == 'hack_indent':
                    # merge identical ident divs
                    if sibling.attrib.has_key('style') and sibling.attrib['style'] == indent_div.attrib['style']:
                        indent_div.append(sibling)
                        hack_divs.remove(sibling)
                        sibling.drop_tag()
                    else:
                        break
                else:
                    indent_div.append(sibling)        
        # remove surrounding div #TODO find a better way
        doc = html.tostring(doc)[5:]
        doc = doc[:-6]
        return doc
    
    _html_escape_left = '__MANABI_HTML_ESCAPE_LEFT__'
    _html_escape_right = '__MANABI_HTML_ESCAPE_RIGHT__'

    def _escape_html(self, text):
        text = text.replace('<', self._html_escape_left)
        text = text.replace('>', self._html_escape_right)
        return text

    def _unescape_html(self, text):
        text = text.replace(self._html_escape_left, '<')
        text = text.replace(self._html_escape_right, '>')
        return text

    def _write_text(self, text, escape_html=True):
        # escape any HTML tags that we are inserting, since sometimes dictionary entries use < and > signs
        # we will unescape these later
        if escape_html:
            text = self._escape_html(text)
        eb_write_text_string(self.book, unicode(text).encode('euc-jp'))

    def _set_hooks(self, content_method):
        heading_hooks = [
            (EB_HOOK_INITIALIZE,          self._hook_initialize),
            (EB_HOOK_BEGIN_SUBSCRIPT,     self._hook_tags),
            (EB_HOOK_END_SUBSCRIPT,       self._hook_tags),
            (EB_HOOK_BEGIN_SUPERSCRIPT,   self._hook_tags),
            (EB_HOOK_END_SUPERSCRIPT,     self._hook_tags),
            (EB_HOOK_BEGIN_EMPHASIS,      self._hook_tags),
            (EB_HOOK_END_EMPHASIS,        self._hook_tags),
            (EB_HOOK_NARROW_FONT,         self._hook_font),
            (EB_HOOK_WIDE_FONT,           self._hook_font),
            (EB_HOOK_BEGIN_DECORATION,    self._hook_tags),
            (EB_HOOK_END_DECORATION,      self._hook_tags),
        ]
        text_hooks = heading_hooks + [
            (EB_HOOK_NEWLINE,             self._hook_new_line),
            (EB_HOOK_SET_INDENT,          self._hook_set_indent),
            (EB_HOOK_BEGIN_KEYWORD,       self._hook_tags),
            (EB_HOOK_END_KEYWORD,         self._hook_tags),
            (EB_HOOK_BEGIN_REFERENCE,     self._hook_tags),
            (EB_HOOK_END_REFERENCE,       self._hook_tags),
            #(EB_HOOK_BEGIN_NARROW,        self._hook_tags),
            #(EB_HOOK_END_NARROW,          self._hook_tags),
        ]
        hooks = {eb_read_heading: heading_hooks, eb_read_text: text_hooks}
        eb_set_hooks(self.hookset, tuple(hooks[content_method]))

    def _hook_initialize(self, book, appendix, container, code, argv):
        return EB_SUCCESS

    def _write_text_anchor(self, book, position):
        subbook_id = str(eb_subbook(self.book))
        entry_id = _position_to_resource_id(position)
        uri = self.uri_dispatcher.uri('entry', subbook=subbook_id, entry=entry_id)
        self._write_text(u'<a name=\"{0}\">'.format(uri))

    #hooks
    #FIXME 'horsey' in chujiten is messed up, see ebview for correct one
    def _hook_new_line(self, book, appendix, container, code, argv):
        self._write_text('<br/>\n')
        return EB_SUCCESS

    def _hook_set_indent(self, book, appendix, container, code, argv):
        if container.debug_mode:
            self._write_text('[{0:x},{1}-i]'.format(argv[0],argv[1]))
            self._write_text('{'+str(eb_tell_text(book))+'}')
            self._write_text('['+str(container.indent_stop_code_count)+']')

        # we often have to use indent levels to determine where the entry properly ends,
        # since it is usually not clearly encoded.
        if not container.first_indent_level:
            container.first_indent_level = argv[1]

        if argv[1] < container.first_indent_level:
            self._write_text(container.EARLY_ENTRY_TERMINATOR)
        elif argv[1] == 1:
            # first indent level is considered a stop code,
            # since it only occurs at the beginning of an entry.
            container.indent_stop_code_count += 1
            
            if container.read_count >= 1 or container.indent_stop_code_count > 1:
                # an unfortunate hack, since sometimes the next entry begins midway through a read
                self._write_text(container.EARLY_ENTRY_TERMINATOR)

        padding_width = 10 * int(argv[1]) #TODO refactor indentation padding constant
        self._write_text(u'<hack_indent style=\"padding-left:{0}\"/>'.format(padding_width))
        return EB_SUCCESS

    #TODO set_indent hook
    def _hook_tags(self, book, appendix, container, code, argv):
        def end_reference():
            subbook_id = str(eb_subbook(self.book))
            entry_id = _position_to_resource_id([argv[1], argv[2]])
            uri = self.uri_dispatcher.uri('entry', subbook=subbook_id, entry=entry_id)
            return u'</a><hack_attribs href=\"{0}\" rel=\"subsection\"/>'.format(uri)
            #TODO sometimes the rel will be an entry/keyword (chapter?), or book, etc.

        def begin_keyword():
            if container.debug_mode:
                self._write_text('[{0:x},{1}]'.format(argv[0],argv[1]))
            self._write_text_anchor(book, eb_tell_text(book))
            return '<span class="keyword">'

        def begin_decoration():
            # argv[1] contains the method
            # 1: italic
            # ?: emphasis (bold?)
            method = argv[1]
            if method == 1 or method == 4353:
                container.decoration_stack = '</em>'
                return '<em>'
            elif method == 4355:
                container.decoration_stack = '</strong>'
                return '<strong>'

        def end_decoration():
            if container.decoration_stack:
                tag = container.decoration_stack
                container.decoration_stack = None
                return tag

        hooks = { EB_HOOK_BEGIN_REFERENCE:    '<a>',
                  EB_HOOK_END_REFERENCE:      end_reference,
                  EB_HOOK_BEGIN_KEYWORD:      begin_keyword,
                  EB_HOOK_BEGIN_NO_NEWLINE:   '<span style="white-space: nowrap;">',
                  EB_HOOK_END_NO_NEWLINE:     '</span>',
                  EB_HOOK_END_KEYWORD:        '</a></span>',
                  EB_HOOK_BEGIN_SUBSCRIPT:    '<sub>',
                  EB_HOOK_END_SUBSCRIPT:      '</sub>',
                  EB_HOOK_BEGIN_SUPERSCRIPT:  '<sup>',
                  EB_HOOK_END_SUPERSCRIPT:    '</sup>',
                  EB_HOOK_BEGIN_EMPHASIS:     '<em>',
                  EB_HOOK_END_EMPHASIS:       '</em>',
                  EB_HOOK_BEGIN_DECORATION:   begin_decoration,
                  EB_HOOK_END_DECORATION:     end_decoration,
        }

        text = hooks.get(code, '?')
        if callable(text):
            text = text()
        if text is not None:
            self._write_text(text)
        return EB_SUCCESS

    def _hook_wave(self, book, appendix, container, code, argv):
        if code == EB_HOOK_BEGIN_WAVE:
            self._write_text('<a>')
        elif code == EB_HOOK_END_WAVE:
            start_offset = (argv[2] - 1) * EB_SIZE_PAGE + argv[3]
            end_offset = (argv[4] - 1) * EB_SIZE_PAGE + argv[5]
            data_size = int(end_offset - start_offset)

            subbook_id = str(eb_subbook(self.book))
            page = int(argv[2])
            offset = int(argv[3])
            audio_id = _position_to_resource_id([page, offset, data_size])
            uri = self.uri_dispatcher.uri('audio', subbook=subbook_id, audio=audio_id)
            self._write_text(u'</a><hack_attribs href=\"{0}\" />'.format(uri))

    #TODO refactor hook code into its own module
    #TODO use eb_narrow_font_character_bitmap for unknown ones, using a img tag whose url has the gaiji id
    def _hook_font(self, book, appendix, container, code, argv):
        # we'll convert the gaiji afterwards, since euc-jp doesn't have everything we need
        self._write_text(self.gaiji_handler.tag(code, argv[0]))
        return EB_SUCCESS




if __name__ == "__main__":

    dict_path = './tests/taishukan/'
    eb_initialize_library()
    #with EpwingBook(dict_path) as my_dict:
    my_dict = EpwingBook(dict_path)
        #/home/alex/dictionaries/chujiten/')

    #for h, c, s, e, u in my_dict.search('test'):
    for e in list(my_dict.search('test', search_method='prefix'))[:5]:
        #print e['heading']
        #print e['content']
        print e.heading
        print e.text
        print '-------'
        #print h
        #print c
        #print(u'{0}:\n{1}'.format(h, c))
    eb_finalize_library()

