def calculateMinimumHP(dungeon: List[List[int]]) -> int:
    '''
    state: dp[i][j] = minimum health needed to reach bottom right from (i, j)
    transition: dp[i][j] = min(dp[i][j + 1], dp[i + 1][j]) - dungeon[i][j]
    base case: dp[n-1][m-1] = 1 if dungeon[n-1][m-1] >= 0 else -dungeon[n-1][m-1] + 1

    Here we are inverting the problem by subtracting the amount of health we gain or lose.
    Any value less than 0 we round it to 1. This is because we can't have negative health.
    '''
    n, m = len(dungeon), len(dungeon[0])

    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    dp[n-1][m-1] = -dungeon[-1][-1] + 1 if dungeon[-1][-1] < 0 else 1

    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if i == n - 1 and j == m - 1: continue
            fromRight = dp[i][j + 1]
            fromBottom = dp[i + 1][j]
            minHealth = min(fromRight, fromBottom) - dungeon[i][j]
            
            dp[i][j] = minHealth if minHealth > 0 else 1

    return dp[0][0]