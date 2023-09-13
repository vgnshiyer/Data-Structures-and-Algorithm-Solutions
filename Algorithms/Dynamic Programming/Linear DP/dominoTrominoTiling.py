from functools import cache

def numTilings(n: int) -> int:
    '''
    state: dp[i][j] -> number of ways to place tiles on a grid of 2xn provided that last tile was a tromino tile or not
    transition: if last tile was a tromino, dp[i][j] = dp[i-1][1] + dp[i-2][0]
                if last tile was a domino, dp[i][j] = dp[i-1][0] + dp[i-2][0] + 2 * dp[i-1][1]
    base case: dp[0][0] = 1
    '''

    mod = 10 ** 9 + 7

    @cache
    def helper(i, isPartial=False):
        if i < 0: return 0
        if i == 0: return 1 if isPartial == False else 0

        if isPartial:
            return (helper(i-1, True) % mod + helper(i-2, False) % mod) % mod

        return (helper(i-1, False) % mod + helper(i-2, False) % mod + 2 * helper(i-1, True) % mod) % mod

    return helper(n) % mod

def numTilings_spaceOptimized(n: int) -> int:
    mod = 10 ** 9 + 7
    if n == 1: return 1

    dp_minus2 = [1, 0]
    dp_minus1 = [1, 0]
    dp = [0, 0]

    for i in range(2, n+1):
        dp = [0, 0]
        dp[0] = (dp_minus1[0] + dp_minus2[0] + 2 * dp_minus1[1]) % mod
        dp[1] = (dp_minus1[1] + dp_minus2[0]) % mod

        dp_minus2 = dp_minus1
        dp_minus1 = dp

    return dp[0]