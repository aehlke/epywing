import unittest

from epywing.history import HistoryManager

class TestHistoryManager(unittest.TestCase):
    
    urls = ['http://www.google.com', 'http://www.python.org/', 'http://pypi.python.org/', 'http://www.reddit.com', 'http://manabi.org']

    def setUp(self):
        self.hist = HistoryManager()
        for url in self.urls:
            self.hist.push(url)

    def test_back_all_the_way(self):
        self.assertEqual(self.hist.current_location, self.urls[-1])
        for _ in range(len(self.urls) - 1):
            url = self.hist.back()
            self.assertEqual(url, self.urls[-(_ + 2)])
            self.assertEqual(self.hist.current_location, url)
    
    def test_back_too_far(self):
        self.test_back_all_the_way()
        self.assertRaises(IndexError, self.hist.back)

    def test_back_and_forward(self):
        self.test_back_all_the_way()
        for _ in range(len(self.urls) - 1):
            url = self.hist.forward()
            self.assertEqual(url, self.urls[_ + 1])

    def test_forward_too_far(self):
        self.assertRaises(IndexError, self.hist.forward)
        self.hist.back()
        self.hist.forward()
        self.assertRaises(IndexError, self.hist.forward)
        self.hist.go(-2)
        self.assertRaises(IndexError, self.hist.go, 10)

    def test_current_location(self):
        h = self.hist
        #h.
        pass



class TestHistoryManager2(unittest.TestCase):
    def setUp(self):
        self.hist = HistoryManager()

    def test_general(self):
        self.hist.push('foo')
        self.hist.push('bar')
        self.assertEqual(self.hist.back(), 'foo')
        self.hist.push('baz')
        self.assertEqual(len(self.hist.forward_items), 0)
        self.assertEqual(self.hist.back_items, ['foo'])
        self.assertTrue('baz' in self.hist)
        self.assertTrue('foo' in self.hist)
        self.hist.push('qux')
        self.assertEqual(self.hist.back_items, ['foo', 'baz'])

        def is_at_qux():
            self.assertEqual(self.hist.current_location, 'qux')
        is_at_qux()
        self.hist.go(-1)
        self.hist.forward()
        is_at_qux()
        self.hist.go(-2)
        self.hist.forward()
        self.hist.go(1)
        is_at_qux()

        self.hist.clear()
        self.assertRaises(IndexError, self.hist.back)
        self.assertEqual(len(self.hist), 0)






