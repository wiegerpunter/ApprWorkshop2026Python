import numpy as np
import hashlib
import mmh3


class CountMin:
    def __init__(self, width, depth):
        self.width = width
        self.depth = depth
        print("Width: ", width, "Depth: ", depth)
        self.cm = np.zeros((depth, width), dtype=int)

    def _hash(self, seed, value):
        # Hash the value using mmh3 and return a non-negative integer
        return mmh3.hash(str(value), seed, False) % self.width

    def update(self, song_id):
        # TODO: update all rows in the count-min sketch for the given song_id
        return


    def query(self, song_id):
        # TODO: return the CountMin estimator for the given song_id
        return 0

    def reset(self):
        self.cm.fill(0)
