import re
from epwingentry import Entry

# This module provides basic URI generation and routing for EPWING books.
# It is not very sophisticated, but it could be used to handle just part of an HTTP URL namespace -- 
# if for example your dictionary was at http://foo.com/dict/, then use your web framework 
# to handle URLs below that, and let any URLs beginning with that be handled by this module.

sub_uri_delimiter = '&'

# Used for displaying several entries together.
collection_uri_prefix = 'collection/'

def route(uri, books):
    '''Routes a URI to a list of resources (typically an EpwingBook Entry) within the given list of `books`, which are EpwingBook instances,
    or a single resource if appropriate.
    A URI may contain "&" characters, which delimits multiple resource URIs.
    '''
    # chop off protocol, if included
    if '://' in uri:
        uri = uri.split('://')[1]

    is_collection = uri[:len(collection_uri_prefix)] == collection_uri_prefix

    if is_collection:
        # chop off the "collection/" part
        uri = uri[len(collection_uri_prefix):]

    resources = []

    for sub_uri in uri.split(sub_uri_delimiter):
        for book in books:
            dispatcher = book.uri_dispatcher

            if dispatcher.matches(sub_uri):
                resource = dispatcher.route(sub_uri)
                if is_collection:
                    resources.append(resource)
                else:
                    return resource
    return resources



class UriDispatcherBase(object):
    def _uri(self, template_name, **kwargs):
        components = ['{0}/{{{0}}}'.format(_) for _ in self.uris[template_name]['components']]
        uri = '/'.join(components).format(**kwargs)
        return uri

    def parse(self, uri):
        '''Returns a dictionary of the URI's components.
        '''
        for name, template in self.uris.items():
            components = [r'{0}/(?P<{0}>[a-zA-Z0-9_-]+)'.format(_) for _ in template['components']]
            regex = '^{0}$'.format('/'.join(components))
            m = re.match(regex, uri)
            if m:
                ret = {'handler': template['handler'], 'components': m.groupdict()}
                return ret

    def route(self, uri):
        '''Returns the resource for the given URI, or None if this book does not contain it.
        '''
        if self.matches(uri):
            match = self.parse(uri)
            return match['handler'](self, **match['components'])


class EpwingUriDispatcher(UriDispatcherBase):
    '''Handles the URIs for a particular EPWING book.
    '''

    def _entry_handler(self, **components):
        from epwing import Entry
        return Entry.from_encoded_location(self.book, components['subbook'], components['entry'])

    uris = {
        'entry': {
            'handler': _entry_handler,
            'components': ('book', 'subbook', 'entry',),
        }
    }

    def __init__(self, book, uri_base='epwing://'):
        ''' `book` is an EpwingBook that this object dispatches URIs for
        '''
        self.book = book
        self.uri_base = uri_base#e.g. /dict/ - this should actually have the book_id in it too

    def uri(self, template_name, **kwargs):
        if 'book' not in kwargs:
            kwargs['book'] = self.book.id
        return self._uri(template_name, **kwargs)

    def matches(self, uri):
        '''Returns whether the given URI is handled by this book.
        '''
        if self.book.subbook:
            subbook_ids = [str(self.book.subbook)]
        else:
            subbook_ids = [subbook['id'] for subbook in self.book.subbooks]
        match = self.parse(uri)
        components = match['components']
        #return False
        return components['book'] == self.book.id \
                and components['subbook'] in subbook_ids





    

