class Solution:
    def numDecodings(self, s: str) -> int:
        mod = 10 ** 9 + 7

        '''
        012
        0*
          1
         9
        9 + 9 * 1 = 18

        * --> 9 * dp[i + 1] + 
        1* --> dp[i + 1] + 9 * dp[i + 2]
        *1 --> 9 * dp[i + 1] + 9 * dp[i + 2]
        ** --> 9 * dp[i + 1] + 81 * dp[i + 2]

        1[1..9], 2[1..6], 3[null]

        *[1..6], 1[0..6] + 2[0..6] = 2 * dp[i + 2]
        *[7..9] += dp[i + 2]

        ** 2, 9 * dp[i + 2] + 6 * dp[i + 2]
        '''

        n = len(s)
        dp = [0] * (n + 1)
        dp[-1] = 1

        for i in range(n - 1, -1, -1):
            if s[i] == '0': continue
            
            if s[i] in '123456789': 
                dp[i] = dp[i + 1] % mod
                if s[i] in '12':
                    if i < n - 1 and s[i + 1] in '1234567890' and int(s[i] + s[i + 1]) <= 26: dp[i] = (dp[i] + dp[i + 2]) % mod
                    elif i < n - 1 and s[i + 1] == '*': dp[i] = (dp[i] + (9 if s[i] == '1' else 6) * dp[i + 2]) % mod
            elif s[i] == '*':
                dp[i] = 9 * dp[i + 1] % mod
                if i < n - 1 and s[i + 1] in '0123456': dp[i] = (dp[i] + 2 * dp[i + 2]) % mod
                elif i < n - 1 and s[i + 1] in '789': dp[i] = (dp[i] + dp[i + 2]) % mod
                elif i < n - 1 and s[i + 1] == '*': dp[i] = (dp[i] + 15 * dp[i + 2]) % mod
        return dp[0] % mod