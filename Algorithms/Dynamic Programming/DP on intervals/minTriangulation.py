'''
It was difficult to get the intuition for this problem as an interval pattern.

- We start at range 0, n - 1. We try selecting the third index k in range [i + 1, j - 1].
- We calculate the value formed by that triangle. We add the minScoreForTriangulation at [i, k] + [k, j].
- We track the min value.
'''
def minScoreTriangulation_iterative(values: List[int]) -> int:
    n = len(values)
    dp = [[0] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(i + 2, n):
            dp[i][j] = float('inf')
            for k in range(i + 1, j):
                dp[i][j] = min(dp[i][j], values[i] * values[j] * values[k] + dp[i][k] + dp[k][j])

    return dp[0][n - 1]
    
def minScoreTriangulation_recursive(values: List[int]) -> int:
    def helper(i, j, dp):
        if j - i <= 1: return 0 # no triangle possible with less than 3 vertices
        if (i, j) in dp: return dp[(i, j)]

        ans = float('inf')
        for k in range(i + 1, j):
            ans = min(ans, values[i] * values[j] * values[k] + helper(i, k, dp) + helper(k, j, dp))
        dp[(i, j)] = ans
        return ans

    return helper(0, len(values) - 1, {}) 