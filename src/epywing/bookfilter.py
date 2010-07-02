from functools import wraps
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


    @classmethod
    def wrap_filter(cls, filter_func):
        '''Decorator for filtering a function's return value.
        '''
        def factory(func):
            @wraps(func)
            def decorator(*args, **kwargs):
                return filter_func(func(*args, **kwargs))
            return decorator
        return factory
