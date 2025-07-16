from bitarray import bitarray
import hashlib


class BloomFilter:
    def __init__(self, size, *hash_functions):
        self.size = size
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)
        self.hash_functions = hash_functions

    def _hash(self, hash_function, item):
        return abs(hash_function(item)) % self.size

    def add(self, item):
        for hash_function in self.hash_functions:
            index = self._hash(hash_function, item)
            self.bit_array[index] = 1

    def might_contain(self, item):
        for hash_function in self.hash_functions:
            index = self._hash(hash_function, item)
            if not self.bit_array[index]:
                return False  # Definitely not in the set
        return True  # Possibly in the set


# Example hash functions using hashlib
def hash_fn1(item):
    return int(hashlib.md5(item.encode()).hexdigest(), 16)


def hash_fn2(item):
    return int(hashlib.sha1(item.encode()).hexdigest(), 16)


def hash_fn3(item):
    return int(hashlib.sha256(item.encode()).hexdigest(), 16)


# Example usage
bloom = BloomFilter(1000, hash_fn1, hash_fn2, hash_fn3)
bloom.add("hello")
print(bloom.might_contain("hello"))  # True
print(bloom.might_contain("world"))  # Probably False
