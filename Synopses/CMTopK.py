import heapq
import math
import sys

from Synopses.CM import CountMin


class CMTopK:
    class Element:
        def __init__(self, song_id, frequency):
            self.song_id = song_id
            self.frequency = frequency

        def __lt__(self, other):
            return self.frequency < other.frequency

    def __init__(self, k, epsilon, delta):
        width = 0 # TODO: size of width based on epsilon
        depth = 0 # TODO: size of depth based on delta
        self.k = k # top-K
        self.cm = CountMin(width, depth)

        # Notice: provided solution uses array here.
        # You can also use a minheap, this is also described in the solutions.

        # self.min_heap = []
        self.topKArray = []
        self.top_k_set = set()
        # max int value
        self.minTopKArray = sys.maxsize

    def update(self, record):
        song_id = record[2]
        # TODO: update the CountMin and the min-heap / array for the top-K elements
        return

    def query(self):
        answer = {}
        for e in self.topKArray:
            answer[e.song_id] = self.cm.query(e.song_id)
        return answer
