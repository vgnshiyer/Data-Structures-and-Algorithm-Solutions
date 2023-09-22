def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        '''
        state: dp[i][prev] = longest subset ending at i, with prev as the last element
        transition: dp[i][prev] = max(dp[i][prev], dp[j][nums[i]] + 1) for all j < i
        base case: dp[i][prev] = 1
        '''
        nums.sort()

        @cache
        def dfs(i, prev = 1):
            if i >= len(nums):
                return ()

            include = ()
            if nums[i] % prev == 0: include = (nums[i], ) + dfs(i + 1, nums[i])

            exclude = dfs(i + 1, prev)

            if len(include) > len(exclude): return include
            return exclude

        return dfs(0, 1)

## using LIS
def largestDivisibleSubset_iterative(nums: List[int]) -> List[int]:
    nums.sort()
    dp = [[x] for x in nums]

    best = [nums[0]]
    for i in range(1, len(nums)):
        cur = dp[i]
        for j in range(i):
            if nums[i] % nums[j] == 0: 
                if len(dp[i]) < len(dp[j]) + 1: dp[i] = dp[j] + cur
        if len(best) < len(dp[i]): best = dp[i]

    return best