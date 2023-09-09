def wiggleMaxLength(self, nums: List[int]) -> int:
    '''
    we either include current element or ignore it from our sequence
    we take the max output from either of the decisions

    state: dp[i][x][0] -> longest wiggle sequence at i, current diff is positive
            dp[i][x][1] -> longest wiggle sequence at i, prev element x, current diff should be negative
    '''

    dp = {}
    def go(i, x, f):
        if i >= len(nums):
            return 0

        if (i, x, f) not in dp:
            # include current element
            include = 0
            if (f and nums[i] - x < 0) or (not f and nums[i] - x > 0):
                include = 1 + go(i+1, nums[i], f ^ 1)

            # exclude current element
            exclude = go(i+1, x, f)

            dp[(i, x, f)] = max(exclude, include)
        return dp[(i, x, f)]

    return 1 + max(go(1, nums[0], 0), go(1, nums[0], 1))

def wiggleMaxLength_iterative(nums: list[int]) -> int:
    '''
    we either include current element or ignore it from our sequence
    we take the max output from either of the decisions

    state: dp[i][x][0] -> longest wiggle sequence at i, current diff is positive
            dp[i][x][1] -> longest wiggle sequence at i, prev element x, current diff should be negative

    transition: dp[i][x][0] = 1 + dp[i+1][nums[i]][1] if x - nums[i] > 0
                dp[i][x][1] = dp[i+1][x][0]
    '''
    m = max(nums) + 1
    dp = [[[0]*2 for _ in range(m)] for _ in range(len(nums) + 1)]
    ans = 1
    for i in range(len(nums)-1, -1, -1):
        for j in range(m):
            if (j - nums[i] > 0): dp[i][j][0] = 1 + dp[i+1][nums[i]][1]
            if (j - nums[i] < 0): dp[i][j][1] = 1 + dp[i+1][nums[i]][0]

            dp[i][j][0] = max(dp[i][j][0], dp[i+1][j][0])
            dp[i][j][1] = max(dp[i][j][1], dp[i+1][j][1])
            ans = max([ans, dp[i][j][0], dp[i][j][1]])

    return ans