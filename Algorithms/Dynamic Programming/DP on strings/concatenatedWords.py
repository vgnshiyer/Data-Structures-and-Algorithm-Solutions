def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
    '''
    ##### Mistakes
    - I iterated over all the words in the dictionary (10 ** 4 possibilities)
    - Instead iterating over all possible substrings from position i is much faster. (30 indices max)
    '''
    res = []
    words = set(words)

    for w in words:
        dp = [0] * (len(w) + 1)
        dp[0] = 1

        for i in range(len(w)):
            if not dp[i]: continue
            for j in range(i, len(w)):
                p = w[i:j+1]
                if p != w and p in words:
                    dp[j + 1] = 1
        if dp[-1]: res.append(w)
    return res