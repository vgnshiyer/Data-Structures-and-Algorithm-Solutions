def tripleStep(n: int, dp: list) -> int:
    if n <= 0: return 0
    if n == 1: return 1

    if dp[n] == -1:
        dp[n] = tripleStep(n-1, dp) + tripleStep(n-2, dp) + tripleStep(n-3, dp)

    return dp[n]

def tripleStepIterative(n):
    dp = [0]*(n+1)
    dp[1] = 1
    for i in range(2, n+1):
        if i-1 >= 0: dp[i] += dp[i-1]
        if i-2 >= 0: dp[i] += dp[i-2]
        if i-3 >= 0: dp[i] += dp[i-3]
    return dp[n]

if __name__ == '__main__':
    n = 6
    dp = [-1]*(n+1)
    print(tripleStep(n, dp)) # 13
    print(tripleStepIterative(n)) # 13