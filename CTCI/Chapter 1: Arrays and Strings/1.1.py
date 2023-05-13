def getIndex(letter) -> int:
    return ord(letter) - 26;

def isUnique(word) -> bool:
    if(len(word) > 26): return False

    mask = 0
    for letter in word:
        index = getIndex(letter)
        if(mask & (1 << index)):
            return False
        mask |= (1 << index)
    return True

if __name__ == '__main__':
    inp1 = 'abcd'
    inp2 = 'abca'

    print(isUnique(inp1))
    print(isUnique(inp2))