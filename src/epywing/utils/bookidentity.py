from plugin import PluginMount

class BookTitle(object):

    __metaclass__ = PluginMount

    def __init__(self, book, *args, **kwargs):
        self.book = book

    def matches(self):
        ''' Determines whether this classification mataches the given EPWING book.
        `self.book` contains the EpwingBook instance.
        '''
        raise NotImplementedError('Subclasses must override this!')
