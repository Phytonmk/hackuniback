import heapq


class Heap(object):
    def __init__(self, initial=None, key=lambda x: x):
        self.key = key
        if initial:
            self._data = [(key(item), item) for item in initial]
            heapq.heapify(self._data)
        else:
            self._data = []

    def push(self, item):
        heapq.heappush(self._data, (self.key(item), item))

    def pop(self):
        return heapq.heappop(self._data)[1]

    def empty(self):
        return len(self._data) == 0

    def top(self):
        item = heapq.heappop(self._data)[1]
        heapq.heappush(self._data, (self.key(item), item))
        return item
