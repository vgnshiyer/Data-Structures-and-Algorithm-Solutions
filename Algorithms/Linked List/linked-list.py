class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List:
    def __init(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
        
    def insert_at(self, data, index):
        if index < 0 or index > self.size:
            raise Exception("Invalid index")
        node = Node(data)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            node.next = current.next
            current.next = node
        self.size += 1

    def get(self, index):
        if index < 0 or index >= self.size:
            raise Exception("Invalid index")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def remove_at(self, index):
        if index < 0 or index >= self.size:
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1