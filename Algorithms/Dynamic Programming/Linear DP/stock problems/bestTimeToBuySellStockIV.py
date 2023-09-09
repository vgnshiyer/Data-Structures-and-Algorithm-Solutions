def maxProfit(k: int, prices: list[int]) -> int:
    '''
    state: dp[i][k][0] -> profit on day i with k transactions and sold
            dp[i][k][1] -> profit on day i with k transactions and buy
    
    transition: dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])

    base: dp[0][k][0] = 0, dp[0][k][1] = -inf
            dp[i][0][0] = 0, dp[i][0][1] = -inf
    '''

    dp = [[[0]*2 for _ in range(k+1)] for _ in range(len(prices) + 1)]
    
    for i in range(k+1):
        dp[0][i][0] = 0
        dp[0][i][1] = -10**4

    for i in range(len(prices) + 1):
        dp[i][0][0] = 0
        dp[i][0][1] = -10**4

    for i in range(1, len(prices) + 1):
        for j in range(1, k+1):
            dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i-1])
            dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i-1])

    return dp[-1][-1][0]

def maxProfit_spaceOptimized(k: int, prices: list[int]) -> int:
    dp = [[0]*2 for _ in range(k+1)]
        
    for i in range(k+1):
        dp[i][0] = 0
        dp[i][1] = -10**4

    dp[0][0] = 0
    dp[0][1] = -10**4

    for i in range(1, len(prices) + 1):
        for j in range(1, k+1):
            dp[j][0] = max(dp[j][0], dp[j][1] + prices[i-1])
            dp[j][1] = max(dp[j][1], dp[j-1][0] - prices[i-1])

    return dp[-1][0]