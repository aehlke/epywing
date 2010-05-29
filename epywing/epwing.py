#!/usr/bin/env python
# -*- coding: utf-8 -*-


#EB API reference http://www.sra.co.jp/people/m-kasahr/eb/doc/eb-09.html

from eb import *
import sys
from os import path
import string
from itertools import izip, cycle
from lxml import html
from lxml.cssselect import CSSSelector

from mybase64 import urlsafe_b64_encode, urlsafe_b64_decode, _num_decode, _position_to_resource_id

from uris import EpwingURIDispatcher
from gaiji import gaiji


#TODO refactor hooks - DRY

class EpwingBook(object):

    def __init__(self, book_path):
        self.book_path = book_path
        self.id = urlsafe_b64_encode(path.basename(self.book_path))
        #TODO verify path is valid
        self.name = unicode(path.basename(self.book_path).decode('euc-jp'))#.title())

        self.uri_dispatcher = EpwingURIDispatcher(self)

        self.book, self.appendix, self.hookset = EB_Book(), EB_Appendix(), EB_Hookset()
        self._set_hooks()

        try:
            eb_bind(self.book, self.book_path)
        except EBError, (error, message):
            code = eb_error_string(error)
            #FIXME raise an exception instead
            sys.stderr.write('Error: %s: %s\n' % (code, message))
            sys.exit(1)

    def __enter__(self):
        eb_initialize_library()
        return self
    
    def __exit__(self, type, value, traceback):
        eb_finalize_library()

    def _set_hooks(self):
        eb_set_hooks(self.hookset, (
            (EB_HOOK_NEWLINE,             self._hook_new_line),
            #(EB_HOOK_NULL,                self._hook_null),
            (EB_HOOK_STOP_CODE,           self._handle_stop_code),
            (EB_HOOK_SET_INDENT,          self._hook_set_indent),
            #(EB_HOOK_BEGIN_CANDIDATE,   self._hook_tags),
            (EB_HOOK_BEGIN_REFERENCE,     self._hook_tags),
            (EB_HOOK_END_REFERENCE,       self._hook_tags),
            (EB_HOOK_BEGIN_KEYWORD,       self._hook_tags),
            (EB_HOOK_END_KEYWORD,         self._hook_tags),
            (EB_HOOK_BEGIN_SUBSCRIPT,     self._hook_tags),
            (EB_HOOK_END_SUBSCRIPT,       self._hook_tags),
            (EB_HOOK_BEGIN_SUPERSCRIPT,   self._hook_tags),
            (EB_HOOK_END_SUPERSCRIPT,     self._hook_tags),
            (EB_HOOK_NARROW_FONT,         self._hook_font),
            (EB_HOOK_WIDE_FONT,           self._hook_font)))

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
        return dict((key, val[1],) for key, val in all_methods.items() if val[0](self.book))

    @property
    def search_methods(self):
        '''Returns a list of the search methods that this dictionary file supports.
        '''
        return self._search_methods.keys()


    #TODO separate URI from ID - have both!?

    @property
    def subbooks(self):
    #TODO def subbooks(cls, book, URI_prefix=''):
        '''Returns a list of the subbooks, with their name, URI and directory, for the current book
        '''
        ret = []
        for subbook in eb_subbook_list(self.book):
            id = str(subbook)
            ret.append({ 'name': eb_subbook_title2(self.book, subbook).decode('euc-jp'),
                         'directory': eb_subbook_directory2(self.book, subbook),
                         'id': id,
                         'uri': self.uri_dispatcher.uri('subbook', subbook_id=id)
            })
        return ret


    def entry(self, entry_id, subbook_id, container=None):
        '''Returns a 2-tuple containing the entry's header and its text contents.
        '''
        entry_locations = map(_num_decode, entry_id.split(_ENTRY_ID_SPLIT))
        if len(entry_locations) == 4:
            heading_location = (entry_locations[0], entry_locations[1], )
            text_location = (entry_locations[2], entry_locations[3], )
            heading = self._get_content(subbook_id, heading_location, container, eb_read_heading)
        elif len(entry_locations) == 2:
            text_location = (entry_locations[0], entry_locations[1], )
            heading = ''
        else:
            return (None, None, ) #TODO error handling
        text = self._get_content(subbook_id, text_location, container, eb_read_text)
        return (heading, text, )


    #TODO
    #def entries(self, from_entry_id, subbook_id, container=None):
    #  pass #yield entries one by one


    #TODO test this
    def audio(self, audio_id, subbook_id):
        eb_set_subbook(self.book, int(subbook_id))
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

    def search(self, query, subbook_id=None, search_method='exact', search_options=None, container=None):
        #TODO what's container?
        if not subbook_id:
            #search all subbooks of this book
            for subbook in self.subbooks:
                for result in self.search(query, subbook['id'], search_method=search_method, search_options=search_options, container=container):
                    yield result
            return

        eb_set_subbook(self.book, int(subbook_id))

        query_encoded = query.encode('euc-jp')
        self._search_methods[search_method](self.book, query_encoded)

        while True:
            hits = eb_hit_list(self.book)
            if not hits:
                break
            for heading_location, text_location in hits:
                heading = self._get_content(eb_subbook(self.book), heading_location, container, eb_read_heading)
                content = self._get_content(eb_subbook(self.book), text_location, container, eb_read_text)
                if string.strip(content):
                    entry_id = _position_to_resource_id([heading_location[0], heading_location[1], text_location[0], text_location[1]])
                    uri = self.uri_dispatcher.uri('entry', subbook_id=subbook_id, entry_id=entry_id)
                    yield (heading, content, subbook_id, entry_id, uri, )

    #TODO separate the heading method
    def _get_content(self, subbook, position, container, content_method, packed=False, entry_count=1):
        eb_set_subbook(self.book, int(subbook))

        self._buffer_entry_count = 0
        self._buffer_start_position = position
        buffer = []
        data = ''
        for i in xrange(200):
            eb_seek_text(self.book, position)
            while True:
                data_chunk = content_method(self.book, self.appendix, self.hookset, container)
                if not data_chunk:
                    break
                buffer.append(data_chunk)
            data += ''.join(buffer)
            buffer = []
            if content_method == eb_read_heading:
                break
            if self._buffer_entry_count >= entry_count:
                break
            eb_forward_text(self.book, self.hookset)
            #ending of content text_status in 4.2 is EB_TEXT_STATUS_HARD_STOP
            #context->text_end_flag = 1 in 3.1
            position = eb_tell_text(self.book)

        data = unicode(data, 'euc-jp', errors='ignore')
        #TODO refactor
        data = string.replace(data, u'\x00', '') #remove null characters, which can break lxml's HTML parser
        data = string.replace(data, u'→§', u'§') #''
        data = string.replace(data, u'＝→', u'＝')
        data = string.replace(data, u'⇒→', u'⇒')
        data = string.replace(data, u'⇔→', u'⇔')
        data = self._fix_html_hacks(data)
        return data


    def _fix_html_hacks(self, text):
        text = u'<div>{0}</div>'.format(text)
        doc = html.fromstring(text)

        #rewrite attributes
        for hack_tag in doc.cssselect('hack_attribs'):
            prev_tag = hack_tag.getprevious()
            attribs = dict((key, val) for key, val in hack_tag.attrib.items())
            prev_tag.attrib.update(attribs)
            hack_tag.drop_tag()

        #fix indentation divs
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
                    #merge identical ident divs
                    if sibling.attrib.has_key('style') and sibling.attrib['style'] == indent_div.attrib['style']:
                        indent_div.append(sibling)
                        hack_divs.remove(sibling)
                        sibling.drop_tag()
                    else:
                        break
                else:
                    indent_div.append(sibling)

        #remove surrounding div #TODO find a better way
        doc = html.tostring(doc)[5:]
        doc = doc[:-6]
        return doc

    def _write_text_anchor(self, book, position):
        subbook_id = str(eb_subbook(self.book))
        entry_id = _position_to_resource_id(position)
        uri = self.uri_dispatcher.uri('entry', subbook_id=subbook_id, entry_id=entry_id)
        eb_write_text_string(book, '<a name=\"{0}\" />'.format(uri))

    #hooks
    #FIXME 'horsey' in chujiten is messed up, see ebview for correct one
    def _hook_new_line(self, book, appendix, container, code, argv):
        eb_write_text_string(book, '<br/>\n')
        #self._write_text_anchor(book, eb_tell_text(book))#eb_write_text_string(book, '<a name=\"{0}\" />'.format(_position_to_resource_id(eb_tell_text(book))))
        return EB_SUCCESS

    def _hook_set_indent(self, book, appendix, container, code, argv):
        padding_width = 10 * int(argv[1]) #TODO refactor indentation padding constant
        eb_write_text_string(book, '<hack_indent style=\"padding-left:{0}\"/>'.format(padding_width))
        return EB_SUCCESS

    def _hook_null(self, book, appendix, container, code, argv):
        #eb_write_text_string(book, 'NULL')
        return EB_SUCCESS

    #TODO set_indent hook
    def _hook_tags(self, book, appendix, container, code, argv):
        def end_reference():
            subbook_id = str(eb_subbook(self.book))
            entry_id = _position_to_resource_id([argv[1], argv[2]])
            uri = self.uri_dispatcher.uri('entry', subbook_id=subbook_id, entry_id=entry_id)
            return '</a><hack_attribs href=\"{0}\" rel=\"subsection\"/>'.format(uri)
            #TODO sometimes the rel will be an entry/keyword (chapter?), or book, etc.

        def begin_keyword():
            self._write_text_anchor(book, eb_tell_text(book))
            return '<span class="keyword">'

        hooks = { EB_HOOK_BEGIN_REFERENCE:    '<a>',
                  EB_HOOK_END_REFERENCE:      end_reference,
                  EB_HOOK_BEGIN_KEYWORD:      begin_keyword,
                  EB_HOOK_END_KEYWORD:        '</span>',
                  EB_HOOK_BEGIN_SUBSCRIPT:    '<sub>',
                  EB_HOOK_END_SUBSCRIPT:      '</sub>',
                  EB_HOOK_BEGIN_SUPERSCRIPT:  '<sup>',
                  EB_HOOK_END_SUPERSCRIPT:    '</sup>',
                  EB_HOOK_BEGIN_EMPHASIS:     '<em>',
                  EB_HOOK_END_EMPHASIS:       '</em>', }

        text = hooks[code]
        if callable(text):
            text = text()
        eb_write_text_string(book, text)
        return EB_SUCCESS

    def _handle_stop_code(self, book, appendix, container, code, argv):
        #eb_write_text_string(book, '[{0},{1}]'.format(argv[0],argv[1]))
        if int(argv[1]) == 1: #end of entry
            self._buffer_entry_count += 1
            eb_write_text_string(book, '<hr>') #TODO entry div tags
        return eb_hook_stop_code(book, appendix, container, code, argv)

    def _hook_wave(self, book, appendix, container, code, argv):
        if code == EB_HOOK_BEGIN_WAVE:
            eb_write_text_string(self.book, '<a>')
        elif code == EB_HOOK_END_WAVE:
            start_offset = (argv[2] - 1) * EB_SIZE_PAGE + argv[3]
            end_offset = (argv[4] - 1) * EB_SIZE_PAGE + argv[5]
            data_size = int(end_offset - start_offset)

            subbook_id = str(eb_subbook(self.book))
            page = int(argv[2])
            offset = int(argv[3])
            audio_id = _position_to_resource_id([page, offset, data_size])
            uri = self.uri_dispatcher.uri('audio', subbook_id=subbook_id, audio_id=audio_id)
            eb_write_text_string(self.book, '</a><hack_attribs href=\"{0}\" />'.format(uri))

    #TODO refactor hook code into its own module
    #TODO use eb_narrow_font_character_bitmap for unknown ones, using a img tag whose url has the gaiji id
    def _hook_font(self, book, appendix, container, code, argv):
        eb_write_text_string(book, gaiji[code].get(argv[0], '<span title=\"{0:x}\">?</span>'.format(argv[0])))
        return EB_SUCCESS


def main():

    dict_path = './taishukan/'
    with EpwingBook(dict_path) as my_dict:
        #/home/alex/dictionaries/chujiten/')

        for h, c, s, e, u in my_dict.search('horse'):
            print(u'{0}:\n{1}'.format(h, c))



if __name__ == "__main__":
    main()
