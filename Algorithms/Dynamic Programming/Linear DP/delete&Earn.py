def deleteAndEarn(nums: list[int]) -> int:
    '''
    state: dp[i] -> max points possible at index i
    transition: dp[i] = max(dp[i-1], cur + dp[ind])
    base case: dp[i] = 0
    '''
    
    nums.sort()

    dp = [0] * len(nums)
    ans = 0
    for i in range(len(nums)):
        cur = nums[i]
        ind = i - 1
        while ind >= 0 and nums[ind] == nums[i]:
            cur += nums[ind]
            ind -= 1

        while ind >= 0 and nums[ind] == nums[i] - 1:
            ind -= 1

        dp[i] = max(dp[i-1], cur + dp[ind])
        ans = max(ans, dp[i])

    return ans