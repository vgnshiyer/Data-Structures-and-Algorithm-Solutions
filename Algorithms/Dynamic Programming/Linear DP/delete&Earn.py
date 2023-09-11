def deleteAndEarn(nums: list[int]) -> int:
    '''
    state: dp[i] -> max points possible at index i
    transition: dp[i] = max(dp[i-1], cur + dp[ind]) where ind is the position which ignores all the elements equal to nums[i] - 1
    base case: dp[i] = 0

    Since we sort the array, we do not have to worry about the elements which are greater than nums[i] + 1, since the state only cares about the best possible solution till index i, while ignoring all the elements greater than nums[i] + 1.
    Consider the current element as 2 at position x. Then all the elements equal to 2 towards the left will be considered, while ignoring all the elements equal to 1 towards the left. The best answer will be computed and stored at dp[x]. While all the elements equal to 3 are being ignored, one may argue that there may be elements equal to 4 are being ignored. But while iterating, when we reach element 4, it will consider the value we stored at dp[x]. So we do not have to worry about the elements greater than nums[i] + 1.
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