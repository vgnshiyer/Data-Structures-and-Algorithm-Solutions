## sort stack, 2.4 is same as this.. just make the push function costlier and other methods in O(1) time

class Stack:
    stack = []

    ## O(n) Time
    def push(self, val) -> None:
        if self.isEmpty() or self.peek() >= val:
            self.stack.append(val)
            return

        temp = self.stack.pop()
        self.push(val)
        self.stack.append(temp)

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def isEmpty(self) -> bool:
        return len(self.stack) == 0

if __name__ == '__main__':
    stack = Stack()

    stack.push(5) # 5
    stack.push(4) # 5, 4
    stack.push(3) # 5, 4, 3
    print(stack.peek()) # 3

    stack.push(6)
    print(stack.peek()) # 3
    print(stack.stack) # 6, 5, 4, 3
    stack.pop()
    print(stack.stack) # 6, 5, 4
