def maxProductPath(grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])
    mod = 10 ** 9 + 7

    dp = [[(-float('inf'), float('inf'))] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = (grid[0][0], grid[0][0])

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1: continue
            topMax, topMin = dp[i - 1][j]
            leftMax, leftMin = dp[i][j - 1]
            cur = grid[i - 1][j - 1]
            if cur == 0:
                dp[i][j] = (0, 0)
                continue

            if cur < 0:
                topMax, topMin = topMin, topMax
                leftMax, leftMin = leftMin, leftMax

            dp[i][j] = (max(cur * topMax, cur * leftMax), min(cur * topMin, cur * leftMin))

    return dp[-1][-1][0] % mod if dp[-1][-1][0] >= 0 else -1