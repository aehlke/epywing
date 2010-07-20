from glob import glob
from os import path

from mybase64 import urlsafe_b64_encode
from epwing import EpwingBook
from itertools import islice
from collections import defaultdict

# these files will identify a directory as an EPWING book
EPWING_IDENTIFYING_FILENAMES = ['CATALOGS', 'catalogs', 'CATALOG', 'catalog',]


class BookManager(object):
    '''Manage a set of epwing dictionaries, to do things like searching all available books.
    `self.books` is a dictionary that maps book ID to EpwingBook instance.
    '''
    def __init__(self):
        self.books = {}

    def add_books(self, *paths, **kwargs):
        '''`paths` is a list of paths to books to add.
        Returns a dictionary that is a subset of `self.books`, containing only the newly added ones.
        `add_each_subbook` makes an EpwingBook isntance for each individual subbook of each book (of which there
        are 1 or more per book). If False, each EpwingBook will represent all the subbooks of each book.
        '''
        new_books = {}
        add_each_subbook = kwargs.get('add_each_subbook', True)

        def add_book(book):
            key = book.id

            # make sure the book supports at least 1 search method
            if not book.search_methods:
                return

            if not self.books.has_key(key):
                new_books[key] = self.books[key] = book

        for book_path in paths:
            try:
                book = EpwingBook(book_path)
            except Exception as e:
                #print e
                # some kind of binding error, so don't import this book - just ignore it, and don't include it in the return value
                #TODO have a better custom exception or something for this so we don't catch all Exceptions
                continue

            # skip this dictionary if this folder name already exists in loaded books.
            # the danger here is that it might not always skip the same book.
            if add_each_subbook:
                for subbook in book.subbooks:
                    subbook2 = EpwingBook(book_path, subbook=subbook['id'], manager=self)
                    add_book(subbook2)
            else:
                add_book(book)

        return new_books

    def remove_book(self, book_id):
        del self.books[book_id]
    
    @property
    def book_paths(self):
        '''Returns a list of the paths for all installed books.
        '''
        return [book.book_path for book in self.books.values()]

    def path_is_epwing_book(self, path_):
        '''Returns whether `path_` is an EPWING book.
        '''
        for filename in EPWING_IDENTIFYING_FILENAMES:
            if path.exists(path.join(path_, filename)):
                return True

        return False

    def find_books_in_path(self, path_, n_deep=2):
        '''Scans the given directory for EPWING books and returns a list of their paths.
        '''
        paths = []

        if self.path_is_epwing_book(path_):
            return [path_]

        for item in glob(path.join(path_, '*')):
            if path.isdir(item) or path.islink(item):
                if self.path_is_epwing_book(item):
                    paths.append(item)
                elif n_deep:
                    paths.extend(self.find_books_in_path(item, n_deep=n_deep - 1))

        return paths

    def _search_and_combine(self, query, books, max_results_per_book=25, **kwargs):
        results = defaultdict(list)

        for book in books:
            for result in islice(book.search(query, **kwargs), 0, max_results_per_book):
                results[result.heading].append(result)

        return results

    def search_all(self, query, max_results_per_book=25, **kwargs):
        '''See EpwingDictionary.search for documentation.
        Returns a dictionary of entry headings mapped to lists of entries which have that heading.
        '''
        return self._search_and_combine(query, self.books.values(), max_results_per_book=max_results_per_book, **kwargs)
    
    def search_category(self, category, query, max_results_per_book=25, **kwargs):
        '''Returns a dictionary of entry headings mapped to lists of entries which have that heading.
        '''
        return self._search_and_combine(query, self.get_books_of_category(category), max_results_per_book=max_results_per_book, **kwargs)

    @property
    def categories(self):
        '''Returns a list of the categories of installed books.
        Sorts by category name.
        '''
        categories = set()

        for book in [b for b in self.books.values() if b.title]:
            categories.update(book.title.categories)

        return sorted(list(categories), key=lambda e: e.label)

    def get_books_of_category(self, category):
        '''Returns a list of books for the given BookCategory.
        '''
        return [book for book in self.books.values() if book.title and category in book.title.categories]

