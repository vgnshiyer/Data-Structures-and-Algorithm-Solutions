@cache
def minInsertions(self, s: str) -> int:
    '''
    state: dp[i][j] -> min insertions to make s[i:j+1] a palindrome
    base case: dp[i][i] = 0
    transition: dp[i][j] = dp[i+1][j-1] if s[i] == s[j]
                            = min(dp[i+1][j], dp[i][j-1]) + 1 if s[i] != s[j]
    '''
    @cache
    def dfs(i, j):
        if i == j: return 0
        if i > j: return 0

        if s[i] != s[j]: return 1 + min(dfs(i + 1, j), dfs(i, j - 1))
        return dfs(i + 1, j - 1)

    return dfs(0, len(s) - 1)

def minInsertions_iterative(s: str) -> int:
    dp = [[0] * (len(s) + 1) for _ in range(len(s) + 1)]

    for i in range(len(s)-1, -1, -1):
        for j in range(i, len(s)):
            if s[i] == s[j]: dp[i][j] = dp[i+1][j-1]
            else: dp[i][j] = 1 + min(dp[i+1][j], dp[i][j-1])

    for r in dp: print(r)
    return dp[0][len(s) - 1]