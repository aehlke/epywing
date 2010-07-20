from functools import wraps
from utils.plugin import PluginMount
from glob import glob
import os
import imp
from functools import partial
from inspect import isgeneratorfunction

class BookFilter(object):
    '''
    Subclasses must implement the following attributes:
    '''
    __metaclass__ = PluginMount

    narrow_gaiji = {}
    wide_gaiji = {}

    def __init__(self, book, *args, **kwargs):
        self.book = book

    def filter_heading(self, entry, heading):
        '''Wraps `Entry.heading`
        '''
        #raise NotImplementedError('Subclasses must override this!')
        return heading

    def filter_text(self, entry, text):
        '''Wraps `Entry.text`
        '''
        return text

    def filter_normalized_heading(self, entry, normalized_heading):
        '''Wraps `Entry.normalized_heading`
        '''
        return normalized_heading

    @classmethod
    def get_filters_for_title(cls, title):
        universal_filters = [plugin_cls for plugin_cls in cls.plugins
                if not hasattr(plugin_cls, 'applies_to')]
        specific_filters = [plugin_cls for plugin_cls in cls.plugins
                if hasattr(plugin_cls, 'applies_to')
                and title.__class__ in plugin_cls.applies_to]
        return universal_filters + specific_filters

    @classmethod
    def filter_gaiji(cls, func):
        '''Decorator for filtering the gaiji tag generation method (`GaijiHandler.tag`).
        '''
        @wraps(func)
        def tag_decorator(self, width_code, index):
            book = self.parent

            for plugin_cls in cls.get_filters_for_title(book.title):
                plugin = plugin_cls(book)

                gaiji = {'h': plugin.narrow_gaiji, 'z': plugin.wide_gaiji}.get(width_code, None)

                if gaiji and index in gaiji:
                    replacement = gaiji[index]

                    if isinstance(replacement, tuple):
                        replacement = replacement[0]
                    if replacement is None:
                        continue
                    else:
                        return replacement

            return func(self, width_code, index)
        return tag_decorator


    @classmethod
    def wrap_filter(cls, filter_name):
        '''Decorator for filtering a method's return value.
        Works on generator functions too.
        Passes kwargs on to filter function.
        Does not execute the filter if the value being filtered is None.
        '''
        def factory(func):
            def execute_filter(entry, value, book, title, *args, **kwargs):
                # Execute any filter that applies to
                # this book's title (if specified).
                if value is not None:
                    for plugin_cls in cls.get_filters_for_title(title):
                        if hasattr(plugin_cls, filter_name):
                            plugin = plugin_cls(book)
                            value = getattr(plugin, filter_name)(entry, value, **kwargs)
                return value

            if isgeneratorfunction(func):
                @wraps(func)
                def decorator(self, *args, **kwargs):
                    book = self.parent
                    title = book.title

                    for ret in func(self, *args, **kwargs):
                        yield execute_filter(self, ret, book, title, *args, **kwargs)
                return decorator
            else:
                @wraps(func)
                def decorator(self, *args, **kwargs):
                    book = self.parent
                    title = book.title

                    ret = func(self, *args, **kwargs)
                    return execute_filter(self, ret, book, title, *args, **kwargs)
                return decorator
        return factory


def load_filter_plugins(directory=os.path.join(os.path.dirname(__file__), 'filters')):
    '''Imports all source files in `directory`, which should contain
    filter plugin subclasses of BookFilter.
    '''
    files = set(glob(os.path.join(directory, '*.py')))

    for file_ in files:
        # simply initializing the plugin is enough to add it to the
        # filter collection, thanks to BookFilter's PluginMount metaclass.
        module_name = os.path.splitext(os.path.basename(file_))[0]
        plugin_module = imp.load_source(module_name, file_)

        
load_filter_plugins()


