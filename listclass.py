__author__ = 'Anton'

import random

class List(object):

    def __init__(self, s):
        self._size = s
        self._list = [None] * s


    def fill_list(self, low, high):

        for x in range(self._size):
            self._list[x] = random.randrange(low, high+1)
