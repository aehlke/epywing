# -*- coding: utf-8 -*-
#
from utils.plugin import PluginMount
from epywing.categories import JapaneseEnglish, EnglishJapanese, Japanese


class BookTitle(object):
    '''Base class for book titles.
    '''
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




# EPWING book titles below

class GeniusEiwaDaijiten(BookTitle):
    #label = 'Genius EiWa Daijiten'
    categories = [JapaneseEnglish]

    def matches(self):
        return u'ジーニアス英和大辞典' in self.book.name


class GeniusEiwaWaeiJiten(BookTitle):
    categories = [JapaneseEnglish, EnglishJapanese]

    def matches(self):
        return u'ジーニアス英和・和英辞典' in self.book.name


class SanseidoSuperDaijirin(BookTitle):
    categories = [Japanese, EnglishJapanese]

    def matches(self):
        return u'三省堂　スーパー大辞林' in self.book.name

