def checkRecord_recursive(n: int) -> int:
    mod = 10 ** 9 + 7

    @cache
    def checkAttendanceRecord(i, l, a):
        if i >= n: return 1
        
        ans = 0
        ## present
        ans += checkAttendanceRecord(i + 1, 0, a)
        ans %= mod

        ## absent
        if a < 1: ans += checkAttendanceRecord(i + 1, 0, a + 1)
        ans %= mod

        ## late
        if l < 2: ans += checkAttendanceRecord(i + 1, l + 1, a)
        ans %= mod

        return ans % mod

    return checkAttendanceRecord(0, 0, 0)

def checkRecord_iterative(n: int) -> int:
    mod = 10 ** 9 + 7
    dp = [[[0] * 2 for _ in range(3)] for _ in range(n + 1)]

    dp[n][0][0] = 1  ## ____P
    dp[n][0][1] = 1  ## _A__P
    dp[n][1][0] = 1  ## ____L
    dp[n][2][0] = 1  ## ___LL
    dp[n][1][1] = 1  ## _A__L
    dp[n][2][1] = 1  ## _A_LL

    for i in range(n - 1, -1, -1):
        dp[i][0][0] = (dp[i + 1][0][0] + dp[i + 1][0][1] + dp[i + 1][1][0]) % mod
        dp[i][0][1] = (dp[i + 1][0][1] + dp[i + 1][1][1]) % mod
        dp[i][1][0] = (dp[i + 1][0][0] + dp[i + 1][0][1] + dp[i + 1][2][0]) % mod
        dp[i][2][0] = (dp[i + 1][0][0] + dp[i + 1][0][1]) % mod
        dp[i][1][1] = (dp[i + 1][0][1] + dp[i + 1][2][1]) % mod
        dp[i][2][1] = dp[i + 1][0][1] % mod

    return dp[0][0][0] % mod

def checkRecord_spaceOptimized(n: int) -> int:
    mod = 10 ** 9 + 7

    P = 1  ## ____P
    AP = 1  ## _A__P
    L = 1  ## ____L
    LL = 1  ## ___LL
    AL = 1  ## _A__L
    ALL = 1  ## _A_LL

    for i in range(1, n + 1):
        P_cur = (P + AP + L) % mod
        AP_cur = (AP + AL) % mod
        L_cur = (P + AP + LL) % mod
        LL_cur = (P + AP) % mod
        AL_cur = (AP + ALL) % mod
        ALL_cur = AP % mod

        P, AP, L, LL, AL, ALL = P_cur, AP_cur, L_cur, LL_cur, AL_cur, ALL_cur

    return P % mod