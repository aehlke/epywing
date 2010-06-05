# -*- coding: utf-8 -*-
#
import unittest

#from epywing.bookmanager import BookManager
from epywing.bookmanager import BookManager
from epywing.epwing import EpwingBook

import os

#class TestEpwing(unittest.TestCase):

#    def setUp(self):
#        self.



def test_epwing_integrations():
    search_path = os.path.split(os.path.abspath(__file__))[0]
    print search_path

    manager = BookManager()

    book_paths = manager.find_books_in_path(search_path)
    print book_paths
    
    manager.add_books(*book_paths)
    ej = manager.books.items()[1][1]
    tai = manager.books.items()[0][1]

    print list(ej.search('cute'))
    list(tai.search(u'horse'))
    list(tai.search(u'horse', search_method='prefix'))[1]

    list(manager.search_all('good'))
    print list(manager.search_all_and_combine_results('good'))


if __name__ == "__main__":
    test_epwing_integrations()


