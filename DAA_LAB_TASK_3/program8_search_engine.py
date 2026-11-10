"""Search engine simulator: binary search vs chained hash vs linear-probe hash."""

WORDS = {
    "algorithm": 101, "binary": 102, "cache": 103, "data": 104, "engine": 105,
    "function": 106, "graph": 107, "hash": 108, "index": 109, "join": 110,
    "key": 111, "list": 112, "memory": 113, "node": 114, "order": 115,
    "pointer": 116, "query": 117, "root": 118, "sort": 119, "tree": 120,
    "union": 121, "value": 122, "weight": 123, "xml": 124, "yield": 125,
    "zone": 126, "array": 127, "buffer": 128, "cursor": 129, "depth": 130,
    "edge": 131, "field": 132,
}


# -------- Binary search --------
class BinarySearchStore:
    def __init__(self, data):
        self.items = sorted(data.items(), key=lambda kv: kv[0])
        self.keys = [k for k, _ in self.items]

    def search(self, word):
        lo, hi = 0, len(self.keys) - 1
        comparisons = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            comparisons += 1
            if self.keys[mid] == word:
                return self.items[mid][1], comparisons
            elif self.keys[mid] < word:
                lo = mid + 1
            else:
                hi = mid - 1
        return None, comparisons


# -------- Hash function --------
def hash_fn(word, size):
    h = 0
    for ch in word:
        h = (h * 31 + ord(ch)) % size
    return h


# -------- Hash with separate chaining --------
class ChainedHash:
    def __init__(self, data, size=17):
        self.size = size
        self.table = [[] for _ in range(size)]
        for k, v in data.items():
            idx = hash_fn(k, size)
            self.table[idx].append((k, v))

    def search(self, word):
        idx = hash_fn(word, self.size)
        probes = 0
        for k, v in self.table[idx]:
            probes += 1
            if k == word:
                return v, probes
        return None, probes if probes else 1


# -------- Hash with linear probing --------
class LinearProbeHash:
    def __init__(self, data, size=61):           # size > 2x data for low load factor
        self.size = size
        self.table = [None] * size
        for k, v in data.items():
            self._insert(k, v)

    def _insert(self, key, value):
        idx = hash_fn(key, self.size)
        while self.table[idx] is not None:
            idx = (idx + 1) % self.size
        self.table[idx] = (key, value)

    def search(self, word):
        idx = hash_fn(word, self.size)
        probes = 0
        while self.table[idx] is not None:
            probes += 1
            if self.table[idx][0] == word:
                return self.table[idx][1], probes
            idx = (idx + 1) % self.size
            if probes > self.size:
                break
        return None, probes if probes else 1


def lookup_all(word, bs, ch, lp):
    v1, c1 = bs.search(word)
    v2, c2 = ch.search(word)
    v3, c3 = lp.search(word)
    return {
        "Binary search":    (v1 is not None, c1),
        "Hash (chaining)":  (v2 is not None, c2),
        "Hash (probing)":   (v3 is not None, c3),
    }


def report(word, bs, ch, lp):
    print(f"\nSearching for '{word}':")
    results = lookup_all(word, bs, ch, lp)
    for method, (found, steps) in results.items():
        status = "FOUND" if found else "NOT FOUND"
        label = "probes" if "Hash" in method else "comparisons"
        print(f"  {method:20s} {status:10s} ({steps} {label})")


def menu():
    bs = BinarySearchStore(WORDS)
    ch = ChainedHash(WORDS)
    lp = LinearProbeHash(WORDS)
    print(f"Loaded {len(WORDS)} words into all three indices.")
    while True:
        word = input("\nSearch word (or 'quit'): ").strip().lower()
        if word in ("quit", "q", ""):
            break
        report(word, bs, ch, lp)


if __name__ == "__main__":
    import sys
    if "--demo" in sys.argv:
        bs = BinarySearchStore(WORDS)
        ch = ChainedHash(WORDS)
        lp = LinearProbeHash(WORDS)
        for w in ["hash", "zone", "array", "notaword", "yield"]:
            report(w, bs, ch, lp)
    else:
        menu()
