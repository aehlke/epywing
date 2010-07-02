# -*- coding: utf-8 -*-
#
from utils.plugin import PluginMount
from epywing.categories import JapaneseEnglish, EnglishJapanese


class BookTitle(object):

    __metaclass__ = PluginMount

    def __init__(self, book, *args, **kwargs):
        self.book = book

    def matches(self):
        ''' Determines whether this classification matches the given EPWING book.
        `self.book` contains the EpwingBook instance.
        '''
        raise NotImplementedError('Subclasses must override this!')

    @classmethod
    def get_title(cls, book):
        '''Returns a subclass instance of BookTitle that identifies the given book instance.
        '''
        for title_class in cls.plugins:
            title = title_class(book)
            if title.matches():
                return title



#class AllTitles(BookTitle):

#    def matches(self, book):
#        return True

# EPWING book titles below

class GeniusEiwaDaijiten(BookTitle):
    #label = 'Genius EiWa Daijiten'
    categories = [JapaneseEnglish]

    def matches(self):
        return u'ジーニアス英和大辞典' in self.book.name


