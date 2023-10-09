def numOfWays(n: int) -> int:
    '''
    Consider that there are two ways to start our traversal.
    1. we have two same colors (121, 323, 131, etc)
    2. we have two different colors (123, 321, 132, etc)

    Our recursion tree looks something like
         121   
        /   \
       212   213
       232   312
       313   (2 ways)
       (3 ways) 

        123
       /   \
      212  231
      232  312
      (2 ways for both)

    With this observation, we define our state as,
    dp[i][0] -> number of ways to paint the ith row with two same colors
    dp[i][1] -> number of ways to paint the ith row with all different colors

    transition:
    dp[i][0] = 3 * dp[i - 1][0] + 2 * dp[i - 1][1]
    dp[i][1] = 2 * dp[i - 1][0] + 2 * dp[i - 1][1]

    base case:
    dp[0][0] = dp[0][1] = 1

    answer: dp[n][0] * 6 + dp[n][1] * 6 (there are 6 different strings with 2 similar, and 6 different strings with 3 different colors)
    '''
    mod = 10 ** 9 + 7

    @cache
    def dfs(i, p):
        if i == 1: return 1

        if p == 0: return ((3 * dfs(i - 1, 0)) % mod + (2 * dfs(i - 1, 1)) % mod) % mod
        return ((2 * dfs(i - 1, 0)) % mod + (2 * dfs(i - 1, 1)) % mod) % mod

    return ((6 * dfs(n, 0)) % mod + (6 * dfs(n, 1)) % mod) % mod

def numOfWays_iterative(n: int) -> int:
    mod = 10 ** 9 + 7

    dp = [[0] * 2 for _ in range(n)]
    dp[0][1] = dp[0][0] = 1

    for i in range(1, n):
        dp[i][0] = ((3 * dp[i - 1][0]) % mod + (2 * dp[i - 1][1]) % mod) % mod
        dp[i][1] = ((2 * dp[i - 1][0]) % mod + (2 * dp[i - 1][1]) % mod) % mod

    return ((6 * dp[-1][0]) % mod + (6 * dp[-1][1]) % mod) % mod

def numOfWays_spaceOptimized(n: int) -> int:
    mod = 10 ** 9 + 7
    twoColor = threeColor = 1

    for i in range(1, n):
        temp1 = ((3 * twoColor) % mod + (2 * threeColor) % mod) % mod
        temp2 = ((2 * twoColor) % mod + (2 * threeColor) % mod) % mod
        twoColor, threeColor = temp1, temp2

    return ((6 * twoColor) % mod + (6 * threeColor) % mod) % mod