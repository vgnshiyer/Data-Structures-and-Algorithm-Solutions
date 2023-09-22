def longestPalindromeSubseq(s: str) -> int:
    '''
    state: dp[i][j] -> longest palindromic subsequence in s[i:j+1]
    transition: dp[i][j] = 2 + dp[i+1][j-1] if s[i] == s[j]
                            = max(dp[i+1][j], dp[i][j-1]) if s[i] != s[j] // we ignore try ignoring either characters if they are not equal
    base case: dp[i][i] = 1
    '''
    @cache
    def dfs(i,j):
        if i == j: return 1
        if i > j: return 0

        if s[i] == s[j]: return 2 + dfs(i + 1, j - 1)
        return max(dfs(i + 1, j), dfs(i, j - 1))

    return dfs(0, len(s) - 1)

def longestPalindromeSubseq_iterative(s: str) -> int:
    dp = [[0] * len(s) for _ in range(len(s))]
    for i in range(len(s)): dp[i][i] = 1

    for i in range(len(s) - 1, -1, -1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]: dp[i][j] = 2 + dp[i + 1][j - 1]
            else: dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][-1]