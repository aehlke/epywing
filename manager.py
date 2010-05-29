
#'''Manage a set of epwing dictionaries, to do things like searching all available books.'''

from glob import glob
from os import path

from mybase64 import urlsafe_b64_encode
from epwing import EpwingBook
from itertools import imap

books = {}

#class InstalledBook(object):
#    '''Represents an EpwingBook which has been 'added' by the user.
#    '''
#    _books = []
    
#    def __init__(self, book):
#        self.book = book
#        InstalledBook._books.append(self)
    
# metadata to keep on each book:
#  order
#  


def add_books(*paths):
    '''`paths` is a list of paths to books to add.
    '''
    for book_path in paths:
        key = urlsafe_b64_encode(path.basename(book_path))
        #skip this dictionary if this folder name already exists in loaded books - the danger here is that it might not always skip the same book
        if not books.has_key(key):
            books[key] = EpwingBook(book_path)

def find_books_in_path(path_):
    '''Scans the given directory for EPWING books and returns a list of their paths.
    '''
    paths = []
    epwing_filenames = ['CATALOGS', 'catalogs', 'CATALOG', 'catalog',]
    for item in glob(path.join(path_, '*')):
        if path.isdir(item) or path.islink(item):
            for filename in epwing_filenames:
                if path.exists(path.join(item, filename)):
                    paths.append(item)
                    break
        else:
            paths.extend(find_books_in_path(item))
    return paths


