def calculateMinimumHP(dungeon: List[List[int]]) -> int:
    '''
    state: dp[i][j] = minimum health needed to reach bottom right from (i, j)
    transition: dp[i][j] = min(dp[i][j + 1], dp[i + 1][j]) - dungeon[i][j]
    base case: dp[n-1][m-1] = 1 if dungeon[n-1][m-1] >= 0 else -dungeon[n-1][m-1] + 1

    Here we are inverting the problem by subtracting the amount of health we gain or lose.
    Any value less than 0 we round it to 1. This is because we can't have negative health.

    Answer to what's the intuition behind populating the DP array backwards ?
    At every index position dp[i][j] the matrix we ask ourselves, what is the minimum health I need to have right here so that I don't die in the future. The answer to this depends on what lies ahead i.e in the future, not what you have encountered so far. When you reach dp[0][0], you exactly know what you need so that you don't die in the future.

    If the question was, whats the maximum value of the orbs you can collect ? - you can solve this both forwards and backwards using either top down or bottom up approach.
    The direction you take sometimes depends on the question being asked.


    Why this problem is different?
    Usually in dp you start from the top and work your way towards the bottom. But in this problem the direction matters. Here you need to start from what you know and work towards a position where you don't know. Because this problem demands for you to make a decision based on the future, not from what you know from the past.
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