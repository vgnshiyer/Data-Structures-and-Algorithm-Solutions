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
    '''
    Why this solution works?
    Consider pairA and pairB, where pairA[1] < pairB[1].
    1. If pairA[1] < pairB[0], then we can add pairA and pairB to our chain.
    2. If pairA[1] >= pairB[0], then we can chain add either pairA or pairB to our chain.
    But consider pairA[1] < pairB[1]. Given this information, we must include pairA to our chain since it has better opportunity to chain with other pairs in the future since its second element is smaller.
    '''
    pairs.sort(key=lambda pair: pair[1])
    maxChainLen = 1
    cur = pairs[0][1]
    for i in range(1, len(pairs)):
        if pairs[i][0] > cur:
            maxChainLen += 1
            cur = pairs[i][1]

    return maxChainLen