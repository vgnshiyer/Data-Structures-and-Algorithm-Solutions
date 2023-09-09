# Dynamic programming approach O(n^2)
def findLongestChain_DP(pairs: List[List[int]]) -> int:
    pairs.sort()

    '''
    state: dp[i] -> longest chain at index i
    transition: dp[i] = max(1 + dp[j], dp[i]) if canChain(i, j)
    base: dp[i] = 1 for all i
    '''

    dp = [1] * len(pairs)
    maxChainLen = 1
    for i in range(1, len(pairs)):
        for j in range(i):
            canChain = pairs[j][1] < pairs[i][0]
            if canChain:
                dp[i] = max(dp[i], 1 + dp[j])
        maxChainLen = max(maxChainLen, dp[i])

    return maxChainLen

# Greedy approach O(nlogn)
def findLongestChain_greedy(pairs: List[List[int]]) -> int:
    pairs.sort(key=lambda pair: pair[1])
    maxChainLen = 1
    cur = pairs[0][1]
    for i in range(1, len(pairs)):
        if pairs[i][0] > cur:
            maxChainLen += 1
            cur = pairs[i][1]

    return maxChainLen