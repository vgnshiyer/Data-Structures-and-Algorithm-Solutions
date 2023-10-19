'''
We use the same minmax method with a slight variation of what we want to track. This time we track the sum of elements remaining after we pick a stone. For this we use prefix sum --> (gets sum in a range in O(1) time and O(n) space)
'''
def stoneGameVII(self, stones: List[int]) -> int:
    n = len(stones)
    pre = [0] * n

    for i in range(n):
        pre[i] = stones[i]
        if i: pre[i] += pre[i - 1]

    dp = [[0] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            points_left = pre[j] - pre[i]
            points_right = pre[j - 1] - (pre[i - 1] if i else 0)                
            dp[i][j] = max(points_left - dp[i + 1][j],
                        points_right - dp[i][j - 1])

    return dp[0][n - 1]