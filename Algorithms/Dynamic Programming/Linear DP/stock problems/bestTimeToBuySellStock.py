def maxProfit(prices: List[int]) -> int:
    '''
    state: dp[i][k][0] -> max pft on day i with k trans and sold
    
    transition: dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])

                dpi0 = max(dpi0, dpi1 + prices[i])
                dpi1 = max(dpi1, dpi00 - prices[i]) 
                since, k here is 1, we can simplify the transition to:
                dpi1 = max(dpi1, 0 - prices[i]) , because dp[anythin][0][0] = 0
    
    base:
        dp[0][k][0] = 0
        dp[0][k][1] = -infi
        dp[i][0][0] = 0
        dp[i][0][1] = -infi
    '''
    maxProfit, leastPrice = 0, -float('inf')
    for p in prices:
        maxProfit = max(maxProfit, leastPrice + p)
        leastPrice = max(leastPrice, -p)
    return maxProfit