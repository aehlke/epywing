from plugin import PluginMount

class BookFilter(object):
    '''
    Subclasses must implement the following attributes:
        narrow_gaiji
        wide_gaiji
    '''
    __metaclass__ = PluginMount

    def filter_heading(self):
        '''
        '''
        #raise NotImplementedError('Subclasses must override this!')
        pass

    def filter_text(self):
        '''
        '''
        #raise NotImplementedError('Subclasses must override this!')
        pass


