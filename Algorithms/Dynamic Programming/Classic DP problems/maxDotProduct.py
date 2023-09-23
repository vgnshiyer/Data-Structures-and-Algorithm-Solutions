def maxDotProduct(n1: List[int], n2: List[int]) -> int:
    '''
    state: dp[i][j] -> max dot product of n1[:i] and n2[:j]
    transition: dp[i][j] = max(dp[i-1][j-1] + n1[i] * n2[j], dp[i-1][j], dp[i][j-1], n1[i] * n2[j])
    base case: dp[len(n1)][len(n2)] = -inf
    '''
def maxDotProduct(n1: List[int], n2: List[int]) -> int:
    @cache
    def dfs(i, j):
        if i >= len(n1) or j >= len(n2): return -float('inf')

        ans = n1[i] * n2[j]
        ans = max(ans, ans + dfs(i + 1, j + 1))
        ans = max([ans, dfs(i + 1, j), dfs(i, j + 1)])
        return ans

    return dfs(0, 0)

def maxDotProduct_iterative(n1: List[int], n2: List[int]) -> int:
    dp = [[-float('inf')] * (len(n2) + 1) for _ in range(len(n1) + 1)]

    for i in range(1, len(n1) + 1):
        for j in range(1, len(n2) + 1):
            cur = n1[i - 1] * n2[j - 1]
            dp[i][j] = max([cur, cur + dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]])
    return dp[-1][-1]

def maxDotProduct_spaceOptimized(n1: List[int], n2: List[int]) -> int:
    dp = [-float('inf')] * (len(n2) + 1)

    for i in range(1, len(n1) + 1):
        temp = [-float('inf')] * (len(n2) + 1)
        for j in range(1, len(n2) + 1):
            cur = n1[i - 1] * n2[j - 1]
            temp[j] = max([cur, cur + dp[j - 1], dp[j], temp[j - 1]])
        dp = temp
    return temp[-1]