## 1.1 is Unique

def getIndex(letter) -> int:
    return ord(letter) - 26;

def getMask(index):
    return (1 << index)

def isUnique(word) -> bool:
    if(len(word) > 26): return False

    bit_vector = 0
    for letter in word:
        index = getIndex(letter)
        mask = getMask(index)
        if(bit_vector & mask):
            return False
        bit_vector |= mask
    return True

if __name__ == '__main__':
    inp1 = 'abcd'
    inp2 = 'abca'

    print(isUnique(inp1))
    print(isUnique(inp2))