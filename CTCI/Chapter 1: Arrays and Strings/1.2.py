def getIndex(letter) -> int:
    return ord(letter) - 26

def compute(word, bit_vector):
    for letter in word:
        index = getIndex(letter)
        bit_vector ^= (1 << index)
    return bit_vector

def checkPermutation(word1, word2):
    bit_vector = 0
    bit_vector = compute(word1, bit_vector)
    bit_vector = compute(word2, bit_vector)

    return bit_vector == 0

if __name__ == '__main__':
    word1 = 'abcd'
    word2 = 'bcad'

    print(checkPermutation(word1, word2))