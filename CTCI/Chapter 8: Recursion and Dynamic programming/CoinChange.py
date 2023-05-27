## standard recursion
def coinChange(sum_: int, coins: list) -> int:
    if sum_ == 0:
        return 1

    nways = 0
    for coin in coins:
        if coin <= sum_:
            nways += coinChange(sum_ - coin, coins)
    return nways

## with memoization
def coinChangeTopDown(sum_: int, coins: list, dp: list) -> int:
    if sum_ == 0:
        return 1

    if dp[sum_] == -1:
        nways = 0
        for coin in coins:
            if coin <= sum_:
                nways += coinChangeTopDown(sum_ - coin, coins, dp)
        dp[sum_] = nways
    
    return dp[sum_]

## iterative
def coinChangeBottomUp(sum_: int, coins: list) -> int:
    dp = [0]*(sum_+1)
    dp[0] = 1 ## 1 way to get a sum_ of 0 with whatever number of coins

    for i in range(1, sum_+1):
        for coin in coins:
            if coin <= i:
                dp[i] += dp[i - coin]
    return dp[sum_]

if __name__ == '__main__':
    print(coinChangeTopDown(5, [2,3,5], [-1]*6))
    print(coinChangeBottomUp(5, [2,3,5]))