## stack of plates

class multiStack:
    stacks = [] # list of stacks
    capacity = 10 # desired length of a single stack
    currentStack = None

    def __init__(self, capacity):
        self.capacity = capacity
        self.currentStack = []

    def push(self, element):
        if(self.isFull()):
            self.stacks.append(self.currentStack)
            self.currentStack = []

        self.currentStack.append(element)
        

    def pop(self):
        if(self.isEmpty()):
            self.currentStack = self.stacks.pop()

        returnVal = self.currentStack.pop()
        return returnVal

    def top(self):
        if(self.isEmpty()):
            self.currentStack = self.stacks.pop()

        returnVal = self.currentStack[-1]
        return returnVal

    def isFull(self):
        return len(self.currentStack) == self.capacity

    def isEmpty(self):
        return len(self.currentStack) == 0

    def popAt(self, index):
        if index <= len(self.stacks) and index >= 1:
            returnVal = self.stacks[index - 1].pop()
        else:
            returnVal = -1

        self.leftShift(index)
        return returnVal

    def leftShift(self, index):
        if index == len(self.stacks) + 1:
            return
        
        smallerStack = self.stacks[index - 1]
        nextStack = self.stacks[index] if index < len(self.stacks) else self.currentStack
        smallerStack.append(nextStack.pop(0))
        self.leftShift(index + 1)

if __name__ == '__main__':
    stack = multiStack(capacity=3)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    ## stack 1 should be full
    print(stack.top()) # print 3

    stack.push(4)
    stack.push(5)
    stack.push(6)
    print(stack.top()) # print 6
    print(stack.stacks)

    stack.pop()
    stack.pop()
    stack.pop()
    print(stack.top()) # print 3

    stack.push(4)
    stack.push(5)
    stack.push(6)
    print(stack.top()) # print 6
    print(stack.stacks)

    print(stack.popAt(1))
    print(stack.stacks, stack.currentStack)
    