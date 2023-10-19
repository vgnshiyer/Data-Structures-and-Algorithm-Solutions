'''
Bottom up DP Solution:
- We calculate prefix sums
- at every range (l, r) -> we partition the array at every index.
- Taking the minimum sum of the two partitions, we get the score for the rest of the partition.
- We maximize this value as we build our dp.

Note: Bottom up is giving TLE -> We are calculating useless states
'''
def stoneGameV(self, stoneValue: List[int]) -> int:
    n = len(stoneValue)
    pre = [0] * n
    for i in range(n):
        pre[i] = stoneValue[i]
        if i: pre[i] += pre[i - 1]

    dp = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            ans = -1
            for k in range(i, j):
                leftP = pre[k] - (pre[i-1] if i else 0)
                rightP = pre[j] - (pre[k] if k >= 0 else 0)
                
                if leftP < rightP:
                    rest = leftP + dp[i][k]
                elif rightP < leftP: 
                    rest = rightP + dp[k + 1][j]
                else:
                    rest = max(leftP + dp[i][k], rightP + dp[k + 1][j])

                ans = max(ans, rest)
            dp[i][j] = ans

    return dp[0][n-1]
    
'''Top-down memoized'''
def stoneGameV(self, stoneValue: List[int]) -> int:
    n = len(stoneValue)
    pre = [0] * n
    for i in range(n):
        pre[i] = stoneValue[i]
        if i: pre[i] += pre[i - 1]

    def dfs(i, j, dp):
        if i >= j: return 0

        if (i, j) in dp: return dp[(i, j)]

        ans = 0
        for k in range(i, j):
            leftP = pre[k] - (pre[i-1] if i else 0)
            rightP = pre[j] - (pre[k] if k >= 0 else 0) 

            if leftP < rightP: res = leftP + dfs(i, k, dp)
            elif rightP < leftP: res = rightP + dfs(k + 1, j, dp)
            else: res = max(leftP + dfs(i, k, dp),
                            rightP + dfs(k + 1, j, dp))
            ans = max(ans, res)
        dp[(i, j)] = ans
        return ans
    return dfs(0, n - 1, {})