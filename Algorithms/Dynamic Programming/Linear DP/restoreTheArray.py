def numberOfArrays(s: str, k: int) -> int:
    '''
    state: dp[i] = number of possible arrays starting at index i
    transition: dp[i] = sum(dp[j + 1]) for all j in range(i, len(s)) if s[i:j+1] is a valid number <= k and >= 1
    base case: dp[-1] = 1
    '''
    mod = 10 ** 9 + 7
    dp = [0] * (len(s) + 1)
    dp[-1] = 1

    for i in range(len(s) - 1, -1, -1):
    for j in range(i, len(s)):
        num = int(s[i:j+1])
        if num >= 1 and num <= k:
        dp[i] = (dp[i] + dp[j + 1]) % mod
        else: break

    return dp[0]