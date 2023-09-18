def minimumDeleteSum(s1: str, s2: str) -> int:
    '''
    state: dp[i][j] -> min ascii sum at index i and j
    transition: dp[i][j] = min(ascii(s[i]) + dp[i+1][j], ascii(s[j]) + dp[i][j+1])
    base case: dp[n][m] = 0
    '''

    memo = {}

    def dfs(i, j):
        if i == len(s1) and j == len(s2): return 0
        if i == len(s1) or j == len(s2):
            res = 0
            while j < len(s2):
                res += ord(s2[j])
                j += 1
            while i < len(s1):
                res += ord(s1[i])
                i += 1
            return res

        if (i, j) not in memo:
            if s1[i] == s2[j]: return dfs(i + 1, j + 1)
            memo[(i, j)] = min(ord(s1[i]) + dfs(i + 1, j), ord(s2[j]) + dfs(i, j + 1))

        return memo[(i, j)]
    
    return dfs(0, 0)

def minimumDeleteSum_iterative(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    s = 0
    for i in range(n + 1):
        s += ord(s1[i - 1]) if i > 0 else 0
        dp[i][0] = s

    s = 0
    for j in range(m + 1):
        s += ord(s2[j - 1]) if j > 0 else 0
        dp[0][j] = s

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]: dp[i][j] = dp[i - 1][j - 1]
            else: dp[i][j] = min(ord(s1[i-1]) + dp[i - 1][j] , ord(s2[j-1]) + dp[i][j - 1])

    return dp[n][m]