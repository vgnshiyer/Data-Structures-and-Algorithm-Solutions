def maxProfit(prices: list[int]) -> int:
    '''
    state: dp[i][k][0] -> max pft on day i with k transactions, provided that we are selling on day i
            dp[i][k][1] -> max pft on day i with k transactions, provided that we are buying on day i

    transition: dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-2][k][0] - prices[i])

    base: dp[1][k][0] = 0, dp[1][k][1] = -prices[1]
    '''
    dp = [[0]*2 for _ in range(len(prices) + 1)]

    dp[0][0], dp[0][1] = 0, -10**4
    dp[1][0], dp[1][1] = 0, -prices[0]

    for i in range(2, len(prices) + 1):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i-1])
        dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i-1])

    return dp[-1][0]

def maxProfit_spaceOptimized(prices: list[int]) -> int:
    dp_i0_pre, dp_i0, dp_i1 = 0, 0, -prices[0]

    for i in range(1, len(prices)):
        dp_i0_old = dp_i0
        dp_i0 = max(dp_i0, dp_i1 + prices[i])
        dp_i1 = max(dp_i1, dp_i0_pre - prices[i])
        dp_i0_pre = dp_i0_old
    return dp_i0