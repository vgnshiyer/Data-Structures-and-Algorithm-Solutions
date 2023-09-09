def maxProfit(prices: list[int], fee: int) -> int:
    '''
    state: dp[i][k][0] -> max pft on day i with k transactions, provided that we are selling on day i
            dp[i][k][1] -> max pft on day i with k transactions, provided that we are buying on day i with a transaction fee

    transition: dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i] - fee)
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k][0] - prices[i])

    base: dp[0][k][0] = 0, dp[0][k][1] = -infi
    '''
    dp_i0, dp_i1 = 0, -10**8

    for i in range(len(prices)):
        dp_i0_old = dp_i0
        dp_i0 = max(dp_i0, dp_i1 + prices[i])
        dp_i1 = max(dp_i1, dp_i0_old - prices[i] - fee)
    return dp_i0