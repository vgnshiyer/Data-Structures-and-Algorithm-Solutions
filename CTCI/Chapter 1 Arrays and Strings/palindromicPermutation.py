## 1.4 palindromic permutation

def palindromicPermutation(word) -> bool:
    bit_vector = getBitVector(word)
    return bit_vector == 0 or exactlyOneBitSet(bit_vector)

def getBitVector(word):
    bit_vector = 0
    for letter in word:
        if letter.isalpha():
            index = getIndex(letter)
            bit_vector = toggle(bit_vector, index)
    return bit_vector

def getIndex(letter):
    return ord(letter) - 26

def toggle(bit_vector, index):
    mask = (1 << index)
    return bit_vector ^ mask

def exactlyOneBitSet(bit_vector):
    return (bit_vector & (bit_vector - 1)) == 0

if __name__ == '__main__':
    inp = 'taco cat'

    print(palindromicPermutation(inp))