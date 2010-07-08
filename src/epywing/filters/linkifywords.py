# -*- coding: utf-8 -*-
from itertools import islice
from epywing.bookfilter import BookFilter
from epywing.utils.mecab import Wakati
from lxml import etree, html
from StringIO import StringIO
import string
import re
import unicodedata
import lxml.html
import cgi

# Linkify vocab words that have exact matches in the given entry.

wakati = Wakati()

# this must be set
book_manager = None


class LinkifyWordsFilter(BookFilter):
    '''This filter turns words in an entry's text into clickable links for searching.
    '''
    #link_template = u'[a href="{url}"]{text}[/a]'
    #link_template = u'<a href="url">{text}</a>'
    link_template = u'<span class="searchable-word" onclick="search(this);">{text}</span>'

    # punctuation characters regex for unicode
    _po_numbers = u'1234567890１２３４５６７８９０'
    _po_extra = u'〈〉（）()←↓↑→⇒⇔＜＞【】《》[]［］〔〕「」『』◇◆★‖｜＝━−‘-〜…=×+＋○°θ▽'
    _po_punc = u''.join(unichr(x) for x in xrange(65536) if unicodedata.category(unichr(x)) == 'Po')
    _po = u''.join([_po_numbers, _po_extra, _po_punc])
    _po = _po.replace(u'\\',u'\\\\').replace(u']', u'\\]') # escape \ and ]
    punctuation_regex = re.compile(u'[' + _po + u']')

    def filter_text(self, text):
        '''`books` is a list of all books to search in when linkifying the entry's text.
        '''
        if hasattr(self.book, 'manager'):
            self.book_manager = self.book.manager
        else:
            # missing book manager
            return text

        # linkify each text fragment, and put them back together
        html_parser = lxml.etree.HTMLParser()
        root = lxml.html.fromstring(text, parser=html_parser)
        fragments = root.xpath('//text()')

        for fragment in fragments:#self._text_fragments(root):
            # replace the fragment in the etree with the linkified text
            parent = fragment.getparent()

            # don't linkify if it's inside an anchor link tag
            if parent.tag == 'a':
                continue

            linkified = self.linkify(cgi.escape(fragment))

            try:
                linkified = etree.XML(u''.join([u'<span>', linkified, u'</span>'])) ##u'<span>' + linkified + u'</span>')#.getroot()#, parser)
            except Exception:
                continue

            if fragment.is_text:
                parent.text = None
                parent.insert(0, linkified)
                # this way is slower, though cleaner since it doesn't insert superfluous <span> tags
                #parent.text = linkified.text
                #for child in reversed(linkified.getchildren()):
                    #parent.insert(0, child)
            else:
                parent.tail = None
                parent.addnext(linkified)
        return etree.tostring(root).decode('utf8')#, encoding='utf8')

    def _exact_match_exists(self, word, _memo={}):
        '''Returns whether there is any exact match in available books.
        '''
        if word in _memo:
            return _memo[word]
        else:
            for book in self.book_manager.books.values():
                if any(book.search(word, search_method='exact')):
                    _memo[word] = True
                    return True
            _memo[word] = False
            return False

    def _is_all_punctuation(self, text, _memo={}):
        '''Returns whether `text` only contains punctuation characters.
        '''
        if text in _memo:
            return _memo[text]
        else:
            _memo[text] = not bool(self.punctuation_regex.sub(u'', text).strip())
            return _memo[text]

    def linkify(self, text):
        '''
        `text` should not contain any HTML
        '''
        words = wakati.split(text)
        if not words:
            return text

        # ignore words that might be HTML entries
        #TODO this is required because of a hack
        html_entities = [u'lt', u'gt']
        words = filter(lambda w: w not in html_entities, words)

        # find each split word in the original text and linkify if needed
        start = 0
        link_positions = []
        for index, word in enumerate(words):
            try:
                offset = text.index(word, start)
                start = offset + len(word)

                # only check this word if it's not punctuation
                if not self._is_all_punctuation(word) \
                        and self._exact_match_exists(word):
                    # match found - we'll add the link later
                    link_positions.append((offset, start,))
            except ValueError:
                continue

        if not link_positions:
            return text

        # when we insert a link, increase the offset by the amount
        # of inserted text, so subsequent link positions are accurate
        offset = 0
        for position in link_positions:
            from_ = position[0] + offset
            to = position[1] + offset
            word = text[from_:to]
            replacement = self.link_template.format(text=word)
            text = u''.join([text[:from_], replacement, text[to:]])
            offset += len(replacement) - len(word)

        return text


            
