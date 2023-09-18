def longestStrChain(self, words: List[str]) -> int:
    '''
    state: dp[i][prev] -> max word chain from this index given the prev word
    transition: dp[i] = max(1 if canChain(prev, cur) else 0 + dp[i+1][cur], dp[i+1][prev])
    base case: dp[n][prev] = 0
    '''

    def canChain(w1, w2):
        if abs(len(w1) - len(w2)) != 1: return False
        foundDiff = False
        i = j = 0
        if len(w1) > len(w2): w1, w2 = w2, w1

        while i < len(w1) and j < len(w2):
            if w1[i] == w2[j]:
                i += 1
                j += 1
            else:
                if foundDiff: return False
                j += 1
                foundDiff = True
        return True

    memo = {}

    def dfs(i, prev=''):
        if i >= len(words): return 0

        if (i, prev) not in memo:
            if prev and not canChain(words[i], prev): return dfs(i + 1, prev)
            memo[(i, prev)] = max(1 + dfs(i + 1, words[i]), dfs(i + 1, prev))
        return memo[(i, prev)]

    words.sort(key=lambda x: (len(x), x))
    return dfs(0)
