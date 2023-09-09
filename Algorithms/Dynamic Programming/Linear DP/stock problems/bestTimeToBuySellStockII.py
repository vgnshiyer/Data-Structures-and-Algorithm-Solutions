def maxProfit(prices: list[int]) -> int:
    '''
    state: dp[i][k][0] -> max profit on day i with at most k transactions, provided that we have sold
            dp[i][k][1] -> max profit on day i with at most k transactions, provided that we bought
    transition: dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k][0] - prices[i])
    base: dp[0][k][0] = 0 (0 profit on day 0)
            dp[0][k][1] = -infi 

            modified transition
    
    minPrice = -infi
    maxPrice = 0

    maxPrice = max(maxPrice, minPrice + prices[i])
    minPrice = max(minPrice, maxPrice_copy - prices[i])
    '''

    maxPrice, minPrice = 0, -10**4
    for i in range(len(prices)):
        maxPrice_copy = maxPrice
        maxPrice = max(maxPrice, minPrice + prices[i])
        minPrice = max(minPrice, maxPrice_copy - prices[i])
    return maxPrice