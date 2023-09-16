def minCut(self, s: str) -> int:
    def isPalindrome(s):
        return s == s[::-1]
    
    @cache
    def helper(i):
        if i >= len(s): return -1

        ans = float('inf')
        for j in range(i, len(s)):
            if isPalindrome(s[i:j+1]):
                ans = min(ans, 1 + helper(j + 1))

        return ans
    
    return helper(0)

def minCut_iterative(s: str) -> int:
    def isPalindrome(s):
        return s == s[::-1]

    dp = [float('inf')] * (len(s) + 1)
    dp[-1] = -1

    for i in range(len(s)-1, -1, -1):
        for j in range(i, len(s)):
            if isPalindrome(s[i:j + 1]): dp[i] = min(dp[i], 1 + dp[j+1])

    return dp[0]

def minCut_optimized(s: str) -> int:
    dp = [float('inf')] * (len(s) + 1)
    dp[-1] = -1
    ispal = [[0] * len(s) for _ in range(len(s))]
    for i in range(len(s)): ispal[i][i] = 1

    for i in range(len(s)-1, -1, -1):
        for j in range(i, len(s)):
            if s[i] == s[j]:
                if j - i == 1: ispal[i][j] = 1 # 2 len palindrome
                elif i < len(s) - 1 and j > 0: ispal[i][j] |= ispal[i + 1][j - 1]

            if ispal[i][j]: dp[i] = min(dp[i], 1 + dp[j + 1])

    return dp[0]