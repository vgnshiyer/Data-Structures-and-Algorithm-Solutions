def distinctSubsequences(s: str, t: str) -> int:
    '''
    state: dp[i][j] -> number of distinct subsequences of s[:i] that equals t[:j]
    transition: dp[i][j] = dp[i-1][j-1] if s[i-1] == t[j-1] else 0 + dp[i-1][j]
    base case: dp[i][0] = 1
    '''

    m, n = len(s), len(t)
    dp = [[0]*(n + 1) for _ in range(m + 1)]

    for i in range(m + 1): dp[i][0] = 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i-1][j] ## without current character in s
            if s[i-1] == t[j-1]: dp[i][j] += dp[i-1][j-1]
    return dp[m][n]

def distinctSubsequences_spaceOptimized(s: str, t: str) -> int:
    m, n = len(s), len(t)
    dp = [0]*(n + 1)
    dp[0] = 1

    for i in range(1, m + 1):
        dp_copy = dp.copy()
        for j in range(1, n + 1):
            if s[i-1] == t[j-1]: dp[j] += dp_copy[j-1]
    return dp[n]