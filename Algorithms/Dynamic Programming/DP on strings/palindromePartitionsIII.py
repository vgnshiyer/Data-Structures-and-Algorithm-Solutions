def palindromePartition(self, s: str, k: int) -> int:
    def cost(i, j):
        numChanges = 0
        while i < j:
            if s[i] != s[j]:
                numChanges += 1
            i += 1
            j -= 1
        return numChanges
    
    @cache
    def helper(i, j):
        if i >= len(s) and j == k: return 0
        if i >= len(s) or j > k: return float('inf')

        ans = float('inf')
        for x in range(i, len(s)):
            ans = min(ans, cost(i, x) + helper(x + 1, j + 1))

        return ans

    return helper(0, 0)

def palindromePartition_iterative(self, s: str, k: int) -> int:
    def cost(i, j):
        numChanges = 0
        while i < j:
            if s[i] != s[j]:
                numChanges += 1
            i += 1
            j -= 1
        return numChanges

    n = len(s)
    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            for x in range(1, i + 1):
                dp[i][j] = min(dp[i][j], cost(x-1, i-1) + dp[x - 1][j - 1])
    return dp[n][k]