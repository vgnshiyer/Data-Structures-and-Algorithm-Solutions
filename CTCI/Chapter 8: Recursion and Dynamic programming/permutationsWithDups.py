permutations = []

def getPermutations(word: str):
    freqMap = {}
    for c in word:
        if c in freqMap:
            freqMap[c] += 1
        else:
            freqMap[c] = 1

    def helper(freqMap: dict, permutation: str):
        if len(permutation) == len(word):
            permutations.append(permutation)
            return
        
        for char, count in freqMap.items():
            if count > 0:
                freqMap[char] -= 1
                helper(freqMap, permutation + char)
                freqMap[char] += 1

    helper(freqMap, '')

if __name__ == '__main__':
    getPermutations('aabbcc')
    print(permutations)

    ## verifying all unique
    print(len(permutations) - len(set(permutations))) ## 0