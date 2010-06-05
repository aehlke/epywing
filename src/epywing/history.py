
#'''Manages user history as they view entries.'''

from mybase64 import urlsafe_b64_encode
from epwing import EpwingBook

from collections import deque


class HistoryManager(object):
    '''Stores entry URI history.
    `self._back` contains the current location as the last entry.
    '''

    def __init__(self, max_history_length=None):
        '''`max_history_length` optionally limits the number of back/forward items in either direction.
        '''
        if max_history_length is not None:
            max_history_length += 1 # to store current location
        self.max_history_length = max_history_length
        self.clear()

    def clear(self):
        self._back = deque(maxlen=self.max_history_length)
        self._forward = deque(maxlen=self.max_history_length)

    @property
    def current_location(self):
        return self._back[-1]

    @current_location.setter
    def current_location(self, value):
        return self.push(value)

    def push(self, uri):
        '''Call this when visiting a new page, with the new page's URI.
        '''
        self._back.append(uri)
        self._forward.clear()

    def back(self):
        '''Returns URI
        '''
        if len(self._back) <= 1:
            # Can't go back when _back contains a single entry,
            # since its last entry is used to store the current location.
            raise IndexError
        self._forward.appendleft(self._back.pop())
        return self.current_location
    
    def forward(self):
        '''Returns URI
        '''
        if not self._forward:
            raise IndexError
        self._back.append(self._forward.popleft())
        return self.current_location

    def go(self, index):
        '''`index` moves history forward if positive, or back is negative.
        '''
        if index < 0:
            go_func = self.back
        elif index > 0:
            go_func = self.forward
        for _ in xrange(abs(index)):
            go_func()
        return self.current_location

    @property
    def back_items(self):
        return list(self._back)[:-1] # remove the current location
    
    @property
    def forward_items(self):
        return list(self._forward)

    def __contains__(self, val):
        return val in self._back or val in self._forward
        
    def __len__(self):
        return len(self.back_items) + len(self.forward_items)

