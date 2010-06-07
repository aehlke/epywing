

from glob import glob
from os import path

from mybase64 import urlsafe_b64_encode
from epwing import EpwingBook
from itertools import islice
from collections import defaultdict

EPWING_IDENTIFYING_FILENAMES = ['CATALOGS', 'catalogs', 'CATALOG', 'catalog',]

class BookManager(object):
    '''Manage a set of epwing dictionaries, to do things like searching all available books.
    '''
    def __init__(self):
        self.books = {}

    def add_books(self, *paths):
        '''`paths` is a list of paths to books to add.
        '''
        for book_path in paths:
            book = EpwingBook(book_path)
            #skip this dictionary if this folder name already exists in loaded books - the danger here is that it might not always skip the same book
            key = book.id
            if not self.books.has_key(key):
                self.books[key] = book

    def find_books_in_path(self, path_):
        '''Scans the given directory for EPWING books and returns a list of their paths.
        '''
        paths = []
        for item in glob(path.join(path_, '*')):
            if path.isdir(item) or path.islink(item):
                for filename in EPWING_IDENTIFYING_FILENAMES:
                    if path.exists(path.join(item, filename)):
                        paths.append(item)
                        break
            else:
                paths.extend(self.find_books_in_path(item))
        return paths


    def search_all(self, query, max_results_per_book=50, **kwargs):
        '''See EpwingDictionary.search for documentation.
        Adds a `book` key-value to each result with the book it came from.
        '''
        for book in self.books.values():
            for result in islice(book.search(query, **kwargs), 0, max_results_per_book):
                #result['book'] = book
                yield result


    #def search_all_combined(self, query, max_results_per_book=50, **kwargs):
    #    '''Searches all books and combines their top 50 (by default) results.
    #    Return a structure like:
    #        [{'heading': 'test', 'results': test_results},]
    #    where `test_results` is a list of search result dicts.
    #    '''
    #    # consume the iterator
    #    results = list(self.search_all(query, max_results_per_book=max_results_per_book, **kwargs))
    #    #print results

    #    # combine the results by `heading` key
    #    combined_results = defaultdict(list)
    #    for result in results:
    #        result2 = result.copy()
    #        #del result2['heading']
    #        #combined_results[result['heading']].append(result2)


    #    # sort the combined results
    #    sorted_results = [{'heading': key, 'results': val} 
    #            for key, val in sorted(combined_results.items())]
    #    return sorted_results



