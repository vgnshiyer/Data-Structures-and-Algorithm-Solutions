def longestDecomposition(self, text: str) -> int:
        n = len(text)
        dp = [[0] * n for _ in range(n)]

        ## this algorithm works but fails for longer inputs.. as  we care calculating states which are never used.
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                l = 0
                dp[i][j] = 1
                while i + l < j - l:
                    if text[i:i+l+1] == text[j-l:j+1]:
                        dp[i][j] = max(dp[i][j], 2 + dp[i + l + 1][j - l - 1])
                    l += 1
        return dp[0][-1]

## recursive memoized solution works better.
def longestDecomposition_recursive(self, text: str) -> int:
    self.memo = {}
    def dp(i,j):
        if i > j:
            return 0
        if i == j:
            return 1
        if (i,j) not in self.memo:
            k = 0
            tmp = 1
            while i+k< j-k:
                if text[i:i+k+1] == text[j-k:j+1]:
                    tmp = max(tmp,2+dp(i+k+1,j-k-1))
                k += 1
            self.memo[(i,j)] = tmp
        return self.memo[(i,j)]
    return dp(0,len(text)-1)