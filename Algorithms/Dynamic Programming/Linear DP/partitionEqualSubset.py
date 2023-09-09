def canPartition(nums: List[int]) -> bool:
    total = sum(nums)
    if total & 1: return False
    total //= 2

    dp = 1
    for n in nums:
        dp |= (dp << n)

    return dp & (1 << total)

def canPartition_iterative(nums):
    total = sum(nums)
    if total & 1: return False
    total //= 2
    n = len(nums)

    dp = [[0] * (total + 1) for _ in range(n + 1)]
    for i in range(n+1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for j in range(total+1):
            dp[i][j] = dp[i - 1][j]
            if j >= nums[i - 1]:
                dp[i][j] |= dp[i - 1][j - nums[i - 1]]

    return bool(dp[n][total])

def canPartition_iterative_space_optimized(nums):
    total = sum(nums)
    if total & 1: return False
    total //= 2
    n = len(nums)

    dp = [0] * (total + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for j in range(total, -1, -1):
            if j >= nums[i - 1]:
                dp[j] |= dp[j - nums[i - 1]]

    return bool(dp[total])

def canPartition_recursive(nums):
    @cache
    def subsetSum(s, i):
        if s == 0: return True
        if i >= len(nums) or s < 0: return False
        return subsetSum(s-nums[i], i+1) or subsetSum(s, i+1)
    total_sum = sum(nums)
    return total_sum & 1 == 0 and subsetSum(total_sum // 2, 0)