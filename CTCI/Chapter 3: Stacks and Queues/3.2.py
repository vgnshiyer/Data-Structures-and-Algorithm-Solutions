## design a stack with push, pop, min in O(1) time

class Stack:
    ## contains elements of type stackNode(data, local_minima)
    ## maintains a global minima
    globalMin = 2**32
    stackNodes = []

    def push(self, val) -> None:
        newnode = stackNode(val, self.globalMin)
        self.stackNodes.append(newnode)
        self.globalMin = min(self.globalMin, val)

    def pop(self) -> int:
        returnNode = self.stackNodes.pop()
        self.globalMin = returnNode.local_min
        return returnNode.data

    def getMin(self) -> int:
        return self.globalMin

class stackNode:
    local_min = -1
    data = -1

    def __init__(self, val, local_min):
        self.data = val
        self.local_min = local_min

if __name__ == '__main__':
    stack = Stack()
    stack.push(5) # min = 5
    stack.push(6) # min = 5
    print(stack.getMin()) # 5

    stack.push(3) # min = 3
    stack.push(7) # min = 3
    print(stack.getMin()) # 3

    stack.pop()
    print(stack.getMin()) # 3
    stack.pop()
    print(stack.getMin()) # 5
    stack.pop()
    print(stack.getMin()) # 5
    stack.pop()
    print(stack.getMin()) # INT_MAX
