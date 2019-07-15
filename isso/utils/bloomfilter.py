class Bloomfilter:
    """A space-efficient probabilistic data structure. False-positive rate:

        * 1e-05 for  <80 elements
        * 1e-04 for <105 elements
        * 1e-03 for <142 elements

    Uses a 256 byte array (2048 bits) and 11 hash functions. 256 byte because
    of space efficiency (array is saved for each comment) and 11 hash functions
    because of best overall false-positive rate in that range.

    >>> bf = Bloomfilter()
    >>> bf.add("127.0.0.1")
    >>> not any(map(bf.__contains__, ("1.2.%i.4" for i in range(256))))
    True

    >>> bf = Bloomfilter()
    >>> for i in range(256):
    ...     bf.add("1.2.%i.4" % i)
    ...
    >>> len(bf)
    256
    >>> "1.2.3.4" in bf
    True
    >>> "127.0.0.1" in bf
    False

    -- via Raymond Hettinger
       http://code.activestate.com/recipes/577684-bloom-filter/
    """

    def __init__(self, array=None, elements=0, iterable=()):
        self.array = array or bytearray(256)
        self.elements = elements
        self.k = 11
        self.m = len(self.array) * 8

        for item in iterable:
            self.add(item)

    def get_probes(self, key):
        h = int(hashlib.sha256(key.encode()).hexdigest(), 16)
        for _ in range(self.k):
            yield h & self.m - 1
            h >>= self.k

    def add(self, key):
        for i in self.get_probes(key):
            self.array[i // 8] |= 2 ** (i % 8)
        self.elements += 1

    def __contains__(self, key):
        return all(self.array[i // 8] & (2 ** (i % 8)) for i in self.get_probes(key))

    def __len__(self):
        return self.elements