def isMatch(s: str, p: str) -> bool:
    @cache
    def dfs(i, j):
        if i >= len(s) and j >= len(p): return True
        if j >= len(p): return False

        if i < len(s) and (s[i] == p[j] or p[j] == '?'): return dfs(i + 1, j + 1)
        elif p[j] == '*':
            with_ = dfs(i + 1, j) if i < len(s) else False
            without_ = dfs(i, j + 1)
            return with_ or without_
        return False
    return dfs(0, 0)

def isMatch_iterative(s: str, p: str) -> bool:
    dp = [[0] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[-1][-1] = 1
    for i in range(len(p)-1, -1, -1):
        if p[i] != '*': break
        dp[-1][i] = 1

    for i in range(len(s) - 1, -1, -1):
        for j in range(len(p) - 1, -1, -1):
            if s[i] == p[j] or p[j] == '?': dp[i][j] = dp[i+1][j+1]
            elif p[j] == '*': dp[i][j] = dp[i+1][j] or dp[i][j+1]
    return dp[0][0]