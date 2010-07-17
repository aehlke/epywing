# -*- coding: utf-8 -*-

from eb import *
from mybase64 import urlsafe_b64_encode, urlsafe_b64_decode, _num_decode, _position_to_resource_id, _ENTRY_ID_SPLIT
from bookfilter import BookFilter
from utils.punctuation import punctuation_regex
from epywing.util import strip_tags, ComparableMixin
import re

class Entry(object, ComparableMixin):
    '''Represents an entry in an EPWING dictionary.
    An entry may have a `heading` (depending on whether the object was created as a result
    of a search, or from a link within another entry), but it will always have `text`.
    '''

    _homonym_index_regex = re.compile(r'<sup>\d+</sup>', re.UNICODE)
    _symbols_regex = re.compile(r'[〈〉（）()【】《》]')
    #_po_extra = u'〈〉（）()←↓↑→⇒⇔＜＞【】《》[]［］〔〕「」『』◇◆★‖｜＝━−‘-〜…=×+＋○°θ▽'

    #normalized_heading_format = u'{heading}'

    ## subentry heading example: 【test 1】~ driver
    ##normalized_subentry_heading_format = u'【{parent}<sup>{index}</sup>】{postfix}'
    #normalized_subentry_heading_format = u'{parent} {postfix}'

    def __init__(self, parent, subbook, heading_location, text_location):
        '''`parent` is an EpwingBook instance.
        #`entry_locations` is a 2- or 4-tuple containing the entry's heading and text offsets.
        '''
        self.parent = parent
        self.subbook = int(subbook)

        self._heading = None
        self._normalized_heading = None
        self._text = None
        self._heading_location = heading_location
        self._text_location = text_location

    @classmethod
    def from_encoded_location(cls, parent, subbook_id, encoded_location):
        '''Returns an Entry instance given an encoded location, like from a URI.
        `location` might contain both a heading and text location, or just the text location,
        depending on the origin of the link (whether from search results, or a reference within a text).
        '''
        locations = map(_num_decode, encoded_location.split(_ENTRY_ID_SPLIT))
        location = (locations[0], locations[1],)
        if len(locations) == 4:
            heading_location = location
            text_location = (locations[2], locations[3],)
        elif len(locations) == 2:
            heading_location = None
            text_location = location
        else:
            raise ValueError
        return cls(parent, subbook_id, heading_location, text_location)

    def __eq__(self, other):
        return self._text_location == other._text_location \
                and self._heading_location == other._heading_location

    def __lt__(self, other):
        '''Attempts to compare first by the most normalized form, then a slightly less 
        normalized form if equal, then by the raw heading.
        '''
        if self.parent is other.parent:
            pass
            #return self._text_location[0] < other._text_location[0]
        
        h1, h2 = self.normalized_heading, other.normalized_heading

        if h1 == h2:
            if hasattr(self, '_homonym_index') and hasattr(other, '_homonym_index'):
                return self._homonym_index < other._homonym_index
            #h1, h2 = strip_tags(self.heading.lower()), strip_tags(other.heading.lower())
            h1, h2 = self._symbols_regex.sub(u'', self.heading.lower()), self._symbols_regex.sub(u'', other.heading.lower())

            if h1 == h2:
                print self.heading
                return self.heading < other.heading
            else:
                return h1 < h2
        else:
            return h1 < h2

    @property
    @BookFilter.wrap_filter('filter_heading')
    def heading(self):
        '''Sometimes we follow a reference link to an entry that doesn't include its heading,
        just the text location, so an Entry instance doesn't always have a heading property.
        '''
        if self._heading_location:
            if not self._heading:
                self._heading = self.parent._get_content(self.subbook, self._heading_location, None, eb_read_heading)
            return self._heading
        else:
            return None

    @property
    @BookFilter.wrap_filter('filter_normalized_heading')
    def normalized_heading(self):
        if not self._normalized_heading:
            heading = self.heading

            # Homonyms usually have <sup>1</sup> etc.
            # Strip it to normalize.
            heading = self._homonym_index_regex.sub(u'', heading)
            heading = strip_tags(heading)
            heading = punctuation_regex.sub(u'', heading)
            heading = heading.strip().lower()
            self._normalized_heading = heading
        return self._normalized_heading

    @property
    @BookFilter.wrap_filter('filter_text')
    def text(self):
        if not self._text:
            self._text = self.parent._get_content(self.subbook, self._text_location, None, eb_read_text)
        return self._text

    @BookFilter.wrap_filter('filter_text')
    def text_iterator(self):
        if not self._text:
            text = u''
            for chunk in self.parent._get_content_iterator(self.subbook, self._text_location, None, eb_read_text):
                text = u''.join([text, chunk])
                yield chunk
            self._text = text
        else:
            yield self._text

    @property
    def id(self):
        if self._heading_location:
            return _position_to_resource_id(list(self._heading_location) + list(self._text_location))
        else:
            return _position_to_resource_id(list(self._text_location))

    @property
    def uri(self):
        return self.parent.uri_dispatcher.uri('entry', subbook=self.subbook, entry=self.id)
