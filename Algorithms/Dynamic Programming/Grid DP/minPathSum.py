def minPathSum(grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    dp[0][1] = dp[1][0] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = grid[i-1][j-1] + min(dp[i - 1][j], dp[i][j - 1])
    return dp[n][m]