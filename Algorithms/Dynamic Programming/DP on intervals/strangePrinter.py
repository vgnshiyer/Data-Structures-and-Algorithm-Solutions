'''
aaab
i  j

While adding j, we have two options
1. Print b separately
2. Try to combine it with an equal character at index (say k) in the range [i, j - 1]
    a. if k == j - 1: dp[i][j] = dp[i][j - 1]
    b. else dp[i][j] = dp[i][k] + dp[k + 1][j - 1]
'''
def strangePrinter(self, s: str) -> int:
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        dp[i][i] = 1
        for j in range(i + 1, n):
            dp[i][j] = dp[i][j - 1] if s[j] == s[j - 1] else 1 + dp[i][j - 1]
            for k in range(i, j-1):
                if s[k] == s[j]:
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j - 1])
    return dp[0][n - 1]