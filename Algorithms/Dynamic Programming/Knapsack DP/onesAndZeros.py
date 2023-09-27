def findMaxForm(strs: List[str], m: int, n: int) -> int:
    countArr = []
    for s in strs:
        nm, nn = 0, 0
        for c in s:
            nm += c == '0'
            nn += c == '1'
        countArr.append((nm, nn))

    @cache
    def dfs(i, m, n):
        if m == 0 and n == 0: return 0
        if i >= len(countArr): return 0

        ans = dfs(i + 1, m, n)
        nm, nn = countArr[i]
        if nm <= m and nn <= n: ans = max(ans, 1 + dfs(i + 1, m - nm, n - nn))
        return ans

    return dfs(0, m, n)

def findMaxForm_iterative(self, strs: List[str], m: int, n: int) -> int:
        countArr = []
        for s in strs:
            nm, nn = 0, 0
            for c in s:
                nm += c == '0'
                nn += c == '1'
            countArr.append((nm, nn))

        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(len(countArr) + 1)]

        for i in range(len(countArr) - 1, -1, -1):
            for j in range(m + 1):
                for k in range(n + 1):
                    dp[i][j][k] = dp[i + 1][j][k]
                    nm, nn = countArr[i]
                    if nm <= j and nn <= k:
                        dp[i][j][k] = max(dp[i][j][k], 1 + dp[i + 1][j - nm][k - nn])
        return dp[0][m][n]