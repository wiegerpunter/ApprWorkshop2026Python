import numpy as np
import hashlib
import math
import mmh3


def _hash(seed, hash_key):
    # positive 64-bit hash value
    return mmh3.hash64(hash_key, seed, signed=False)[0]


def _comp_hashkey(song_id, user_id):
    # make a composite hash key by combining song_id and user_id
    return 0


class FM:
    def __init__(self, epsilon, delta):
        # number of hash functions needed to achieve the desired error and confidence
        self.num_hashes = math.ceil(math.log(1 / delta) / math.log(2) / (epsilon ** 2))
        self.bitmap_size = 64
        self.sketch = np.zeros((self.num_hashes, self.bitmap_size), dtype=bool)

    def _lsb(self, value):
        return (value & -value).bit_length() - 1  # Fast way to get the position of the least significant bit

    def update(self, record):
        song_id, user_id = record[1], record[2]
        # TODO: composite hash key
        # TODO: update sketch for every repetition

    def query(self):
        R = []
        # Placeholder:
        R = [1]
        # TODO: for each repetition, find the position of the least significant bit that is not set to 1
        # TODO: if all bits are set, return bitmap_size

        constant = 1.2928
        avg_R = sum(R) / len(R)
        return int(math.pow(2, avg_R) * constant)

    def reset(self):
        self.sketch.fill(False)
