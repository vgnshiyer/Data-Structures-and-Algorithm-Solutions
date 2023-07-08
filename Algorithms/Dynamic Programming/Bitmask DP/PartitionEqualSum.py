'''
Given an array nums of integers, find whether two subsets exist whose sums are equal.
eg. nums = [1,5,11,5]
ans: true
subsets = {[1,5,5],[11]}

Intuition: 
- this can be treated as a 0/1 knapsack problem.
- we either include the current element or ignore it.
- so the state of our dp becomes (dp[i][j] -> is there a subset of sum j possible with i elements)
- our answer will be dp[n][total//2] -> is there a sum of half the total sum possible with all elements in the array
- notice that this completely changes the problem statement to :- find a subset of the array which sums to a value (say x)

state: dp[i][j] -> whether a sum of j is possible at position i, with i elements
transition: dp[i][j] = dp[i-1][j] || dp[i-1][j-nums[i-1]] (with and without (OR'ed))
base case: dp[anything][0] = True (a sum of zero is possible with any number of elements by simply ignoring it)

Below are some solutions using classic dp approach
'''

## top-down dp - with memoization
def canPartition(self, nums: List[int]) -> bool:
    total = sum(nums)
    nums.sort()

    dp = [[-1 for _ in range(total + 1)] for _ in range(len(nums)+1)]
    def partition(i, s):
        if total - s == s:
            return True

        if dp[i][s] == -1:
            dp[i][s] = False
            for k in range(i, len(nums)):
                dp[i][s] = partition(k + 1, s + nums[k])
                if dp[i][s]: break
        return dp[i][s]
    
    return partition(0, 0)

## bottom-up dp - with tabulation
def canPartition(self, nums):
    total = sum(nums)
    if total & 1: return False
    total //= 2
    n = len(nums)

    dp = [[0] * (total + 1) for _ in range(n + 1)]
    for i in range(n+1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1,total+1):
            dp[i][j] = dp[i - 1][j]
            if j >= nums[i - 1]:
                dp[i][j] |= dp[i - 1][j - nums[i - 1]]

    return bool(dp[n][total])

## bottom-up dp - space optimized
def canPartition(self, nums):
    total = sum(nums)
    if total & 1: return False
    total //= 2
    n = len(nums)

    dp = [False for _ in range(total + 1)]
    dp[0] = True

    for num in nums:
        dp_copy = dp.copy()
        for j in range(num,total+1):
            dp[j] |= dp_copy[j - num]

    return dp[total]

## bitmask-dp
## this is the fastest solution -> (We only care about the true values, therefore only care about shifting the true values by num places on every iteration)
def canPartition(self, nums: List[int]) -> bool:
    total = sum(nums)
    if total & 1: return False
    total //= 2

    dp = 1
    for num in nums:
        dp |= dp << num
    return dp & (1 << total)