def countPalindromicSubsequences(self, s: str) -> int:
    n = len(s)
    mod = 10 ** 9 + 7
    dp = [[0] * n for _ in range(n)]

    '''
    An alternative way to iterate through the dp is
    for d in range(1, n):
        for i in range(n-d):
            j = i + d
    We work our way from the smaller windows from left to right to the larger windows
    '''
    for i in range(n-1, -1, -1):
        for j in range(i, n):
            if i == j:
                dp[i][j] = 1
                continue
            if i == n-1 or j == 0: continue
            if s[i] != s[j]:
                dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]
            else:
                # eg. a __ a
                l, r = i + 1, j - 1

                while l <= r and s[l] != s[j]: l+=1
                while l <= r and s[r] != s[i]: r-=1

                if l > r: ## all different chars in between
                    dp[i][j] = dp[i + 1][j - 1] * 2 + 2
                    ## {b} * 2 = {b, aba}
                    ## {a, aa} -> added 2
                elif l == r: ## one similar char in between
                    dp[i][j] = dp[i + 1][j - 1] * 2 + 1
                    ## {a} * 2 = {a, aaa}
                    ## {aa} [s[i] + s[j]] -> added 1
                else: ## more than two similar char in between
                    dp[i][j] = dp[i + 1][j - 1] * 2 - dp[l + 1][r - 1]
                    ## {aa, aba, ...} * 2 = {aaaa, aabaa, ...}
                    ## remove dp[l + 1][r - 1] as it is being counted twice by dp[i + 1][j - 1] * 2
            dp[i][j] = dp[i][j] + mod if dp[i][j] < 0 else dp[i][j] % mod

    return dp[0][-1]