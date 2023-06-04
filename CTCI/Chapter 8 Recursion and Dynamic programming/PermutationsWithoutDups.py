permutations = []

def getPermutations(word: list, start: int, end: int) -> None:
    if start > end:
        permutations.append(word.copy())
        return

    for i in range(start, end+1):
        word[start], word[i] = word[i], word[start]
        getPermutations(word, start+1, end)
        word[start], word[i] = word[i], word[start]

if __name__ == '__main__':
    getPermutations(['a','b','c'], 0, 2)
    print(permutations)