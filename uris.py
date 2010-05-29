

class EpwingURIDispatcher(object):
    '''Handles the URIs for a particular EPWING book.
    '''
    uri_templates = {
            'entry': 'book/{book_id}/subbook/{subbook_id}/entry/{entry_id}',
            'subbook': 'book/{book_id}/subbook/{subbook_id}',
            'audio': 'book/{book_id}/subbook/{subbook_id}/audio/{audio_id}'
    }

    def __init__(self, book, uri_base='/'):
        ''' `book` is an EpwingBook that this object dispatches URIs for
        '''
        uri_base = '/' 
        self.book = book
        self.uri_base = uri_base#e.g. /dict/ - this should actually have the book_id in it too

    def _uri(self, template_name, **kwargs):
        return self.uri_base + self.uri_templates[template_name].format(**kwargs)

    def uri(self, template_name, **kwargs):
        if 'book_id' not in kwargs:
            kwargs['book_id'] = self.book.id
        return self._uri(template_name, **kwargs)



    

