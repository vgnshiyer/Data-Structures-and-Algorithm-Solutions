def numTrees(n: int) -> int:
    '''
    state: dp[i] -> number of ways to form unique BSTs with n nodes
    transition: dp[i] = dp[j-1] * dp[i-j] (for j in 1 to i)
    base: dp[0] = 1, dp[1] = 1
    '''
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            dp[i] += dp[j-1] * dp[i-j]
    return dp[-1]