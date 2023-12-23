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
        '''
        Sets a key val pair in the hash_table.

        If the key gets hashed to the same value as some other key,
        chains the new value in to the table at the hashed index.
        '''
        hash_index = self._hash_function(k)
        for item in self.table[hash_index]:
            if item.key == k:
                item.val = v
                return
        self.table[hash_index].append(Item(k, v))

    def get(self, k):
        '''
        Gets the value for a given key.

        If key not present in the hashed index,
        returns an ItemNotFoundException
        '''
        hash_index = self._hash_function(k)
        for item in self.table[hash_index]:
            if item.key == k: return item.val
        raise ItemNotFoundException

    def remove(self, k):
        '''
        Removes an item from the hashed index with the given key.

        If item not present at hashed index,
        returns an ItemNotFoundException
        '''
        hash_index = self._hash_function(k)
        for index, item in enumerate(self.table[hash_index]):
            if item.key == k:
                del self.table[hash_index][index]
                return
        raise ItemNotFoundException

    def __contains__(self, k):
        '''
        Implements the python "in" keyword.

        Returns true if an item is present with key == k
        '''
        hash_index = self._hash_function(k)
        for item in self.table[hash_index]:
            if item.key == k:
                return True
        return False

class ItemNotFoundException(Exception):
    pass