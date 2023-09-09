def maxProfit(prices: list[int]) -> int:
    '''
    state: dp[i][k][0] -> max pft on day i with k trans and sold
    transition: dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])

                optimizing space:
                dp_i10_copy
                dp_i10 = max(dp_i10, dp_i11 + prices[i])
                dp_i11 = max(dp_i11, 0 - prices[i])

                dp_i20 = max(dp_i20, dp_i21 + prices[i])
                dp_i21 = max(dp_i21, dp_i10_copy - prices[i])
    base:
    dp[0][k][0] = 0
    dp[0][k][1] = -infi
    dp[i][0][0] = 0
    dp[i][0][1] = -infi
    '''

    dp_i10 = 0
    dp_i11 = -10**4
    dp_i20 = 0
    dp_i21 = -10**4

    for i in range(len(prices)):
        dp_i10_copy = dp_i10
        dp_i10 = max(dp_i10, dp_i11 + prices[i])
        dp_i11 = max(dp_i11, 0 - prices[i])

        dp_i20 = max(dp_i20, dp_i21 + prices[i])
        dp_i21 = max(dp_i21, dp_i10_copy - prices[i])
    return dp_i20