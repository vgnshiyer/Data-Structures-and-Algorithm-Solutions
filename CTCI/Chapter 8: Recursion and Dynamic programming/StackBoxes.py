class box:
    height: int
    width: int
    length: int

    def __init__(self, height, width, length):
        self.height = height
        self.width = width
        self.length = length

def canPlace(box1: box, box2: box) -> bool:
    if not box2: return True
    return box1.height <= box2.height and box1.width <= box2.width and box1.length <= box2.length

def stackBoxes(stack: list, index: int, memo: list, previous: box = None) -> int:
    if index >= len(stack):
        return 0

    currentBox = stack[index]

    if canPlace(currentBox, previous):
        if memo[index] == -1:
            memo[index] = currentBox.height + stackBoxes(stack, index + 1, memo, currentBox)
        heightWithCurrentBox = memo[index]
    else:
        heightWithCurrentBox = -1

    heightWithoutCurrentBox = stackBoxes(stack, index + 1, memo, previous)

    return max(heightWithCurrentBox, heightWithoutCurrentBox)

if __name__ == '__main__':
    stackOfBoxes = [box(12, 14, 8), box(2, 12, 8), box(7, 5, 10), box(15, 15, 15)]

    stackOfBoxes.sort(key=lambda x: x.height, reverse=True)
    memo = [-1]*len(stackOfBoxes)
    maxHeight = stackBoxes(stackOfBoxes, 0, memo)
    print(maxHeight)