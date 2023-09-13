from functools import cache

'''
state: dp[0] -> largest sum with remainder 0 when divided by 3
        dp[1] -> largest sum with remainder 1 when divided by 3
        dp[2] -> largest sum with remainder 2 when divided by 3

transition: dp[0] = max(dp[0], current + dp[current % 3])
            dp[1] = max(dp[1], current + dp[(current + 1) % 3]) 
            dp[2] = max(dp[2], current + dp[(current + 2) % 3])

base case: dp = [0, -inf, -inf]
'''

def maxSumDivThree(self, nums: List[int]) -> int:
    @cache
    def helper(i, j):
        if i >= len(nums): return j if j % 3 == 0 else 0

        return max([j if j % 3 == 0 else 0, helper(i+1, j), helper(i+1, j + nums[i])])
    return helper(0, 0)

'''
Above solution works but fails with a memory error -> Since there can be around 10**4 numbers and the sum can be very large, we can only store so many values for j. That is too much memory. 

Instead of storing the actual sum, we can store the remainder when dividing by three. That way out j will be limited from 0 to 2.
'''

def maxSumDivThree(self, nums: List[int]) -> int:
    @cache
    def helper(i, j):
        if i >= len(nums): return 0 if not j else -10**9

        return max(helper(i+1, j), nums[i] + helper(i+1, (j + nums[i]) % 3))
    return helper(0, 0)

def maxSumDivThree_iterative(self, nums: List[int]) -> int:
    dp = [[0]*3 for _ in range(len(nums) + 1)]
    dp[0][1] = -10**9
    dp[0][2] = -10**9

    for i in range(1, len(nums) + 1):
        dp[i][0] = max(dp[i-1][0], nums[i-1] + dp[i-1][nums[i-1] % 3])
        dp[i][1] = max(dp[i-1][1], nums[i-1] + dp[i-1][(1 + nums[i-1]) % 3])
        dp[i][2] = max(dp[i-1][2], nums[i-1] + dp[i-1][(2 + nums[i-1]) % 3])

    return dp[-1][0]

def maxSumDivThree_spaceOptimized(self, nums: List[int]) -> int:
    dp = [0, -10**9, -10**9]

    for i in range(1, len(nums) + 1):
        dp_copy = dp.copy()
        dp[0] = max(dp_copy[0], nums[i-1] + dp_copy[nums[i-1] % 3])
        dp[1] = max(dp_copy[1], nums[i-1] + dp_copy[(1 + nums[i-1]) % 3])
        dp[2] = max(dp_copy[2], nums[i-1] + dp_copy[(2 + nums[i-1]) % 3])

    return dp[0]