'''
__str__ : represent class objects as a string
__repr__ : returns a printable version of an object -> must be used for debugging -> python falls to this method if __str__ is not implemented
'''

from hash_table import HashMap, ItemNotFoundException

class Item:
    def __init__(self, query, results):
        self.prev = None
        self.next = None
        self.query = query
        self.results = results

    def __repr__(self):
        return f'Item({self.query}, {self.results})'

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def _to_front(self, node: Item) -> None:
        if self.head == node:
            self.head = node.next

        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        node.next = None

    def update(self, node: Item) -> None:
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        self._to_front(node)

    def insert(self, node: Item):
        if not self.tail:
            self.head = node
            self.tail = node
        else:
            self._to_front(node)
        node.next = None
    
    def reduce_size(self):
        if self.head is not None:
            if self.head.next is not None:
                self.head.next.prev = None
            self.head = self.head.next
        else:
            print("Cannot reduce size, the list is already empty.")

    def __str__(self):
        temp = self.head
        op = ''
        i = 0
        while temp:
            op += f' -> {temp.results}' 
            temp = temp.next
        return op[4:]

class Cache:
    def __init__(self, max_size):
        self.max_size = max_size
        self.cur_size = 0
        self.hash_table = HashMap(self.max_size)
        self.linked_list = LinkedList()

    def set(self, query, results):
        '''
        Stores the results of the query in cache.

        If query result was already present, stores the updated results. If the
        size of the cache exceeds, it removes the least recently used query result
        from the cache.
        '''
        if query in self.hash_table:
            item = self.hash_table.get(query)
            item.results = results
            self.linked_list.update(item)
        else:
            new_item = Item(query, results)
            self.hash_table.set(query, new_item)
            self.linked_list.insert(new_item)
            self.cur_size += 1
            if self.cur_size > self.max_size:
                removed_query = self.linked_list.head.query
                self.linked_list.reduce_size()
                self.hash_table.remove(removed_query)

    def get(self, query):
        '''
        Gets the results of query stored in cache.

        If query was not cached, returns an ItemNotFoundException
        '''
        try:
            item = self.hash_table.get(query)
            self.linked_list.update(item)
            return item.results
        except ItemNotFoundException as e:
            raise e
