class Item:
    def __init__(self, k, v):
        self.key = k
        self.val = v

class HashMap:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]
        self._hash_function = lambda x : x % self.size

    def set(self, k, v):
        hash_index = self._hash_function(k)
        for item in self.table[hash_index]:
            if item.key == k:
                item.val = v
                return
        self.table[hash_index].append(Item(k, v))

    def get(self, k):
        hash_index = self._hash_function(k)
        for item in self.table[hash_index]:
            if item.key == k: return item.val
        raise ItemNotFoundException

    def remove(self, k):
        hash_index = self._hash_function(k)
        for index, item in enumerate(self.table[hash_index]):
            if item.key == k:
                del self.table[hash_index][index]
                return
        raise ItemNotFoundException

    def __contains__(self, k):
        hash_index = self._hash_function(k)
        for item in self.table[hash_index]:
            if item.key == k:
                return True
        return False

class ItemNotFoundException(Exception):
    pass