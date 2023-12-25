class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.nxt = None

    def __repr__(self):
        return f'Node({self.prev} <- {self.val} -> {self.nxt})'

class CircularArray:
    '''
        --- Circular Array ---
        * A fixed size array.
        * Values can be added to the front or to the back
        * Double ended queue
        * When array is full:
            - Can either block add operations.
            - Can overwrite existing values.
    '''
    def __init__(self):
        null_node = self._create_node(-1)
        self.front = null_node
        self.back = null_node

        self.size = 0

    def _create_node(self, val):
        return Node(val)

    # O(1)
    def add_front(self, val) -> None:
        new_node = self._create_node(val)
        new_node.nxt = self.front
        self.front.prev = new_node
        self.front = new_node
        self.size += 1

    # O(1)
    def remove_front(self) -> int:
        cur_node = self.front
        self.front = self.front.nxt
        self.front.prev = None

        ret_val = cur_node.val
        cur_node = None
        self.size -= 1
        return ret_val

    # O(1)
    def add_back(self, val) -> None:
        new_node = self._create_node(val)
        new_node.prev = self.back
        self.back.nxt = new_node
        self.back = new_node
        self.size += 1

    # O(1)
    def remove_back(self) -> int:
        cur_node = self.back
        self.back = self.back.prev
        self.back.nxt = None

        ret_val = cur_node.val
        cur_node = None
        self.size -= 1
        return ret_val

    def __len__(self):
        return self.size

    def _is_null_node(self, node):
        return node.val == -1

    def __iter__(self):
        cur = self.front
        while cur:
            if self._is_null_node(cur):
                cur = cur.nxt
                continue
            yield cur.val
            cur = cur.nxt

    def is_empty(self):
        return self.size == 0

    # O(n) time
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            raise CircularArrayIndexOutOfRange

        cur = self.front
        while index > 0 and cur:
            if self._is_null_node(cur):
                cur = cur.nxt
                continue
            index -= 1
            cur = cur.nxt
        return cur.val

    def __str__(self):
        return '[' + ', '.join(str(item) for item in self) + ']'

class CircularArrayIndexOutOfRange(Exception):
    pass

if __name__ == '__main__':
    arr = CircularArray()

    arr.add_front(1)
    arr.add_front(2)
    arr.add_front(3)
    arr.add_back(4)
    arr.add_back(5)
    arr.add_back(6)

    assert len(arr) == 6
    assert str(arr) == '[3, 2, 1, 4, 5, 6]'

    arr.remove_front()
    arr.remove_back()

    assert len(arr) == 4
    assert str(arr) == '[2, 1, 4, 5]'

    assert arr.get(0) == 2
    assert arr.get(3) == 5

    for ele in arr:
        print(ele)
    