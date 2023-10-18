'''
Instead of deciding whether to burst current baloon now, we decide whether to burst it at last. That way, we do not have to worry about passing the updated array from furthur states. 

state: dp[l][r] -> max score that can be obtained in this range. 
transition: dp[l][r] = max(dp[l][r], nums[l-1] * nums[i] * nums[r+1] + dp[l][i-1] + dp[i+1][r])

Notice that we multiply nums[l-1] and nums[r+1] because these are the baloons left outside of the range. --> when all baloons in the range will burst, these will remain.
'''

def maxCoins_recursive(nums: List[int]) -> int:
    nums = [1] + nums + [1]

    @cache
    def dfs(l, r):
        if l > r: return 0

        ans = -float('inf')
        for i in range(l, r + 1):
            ans = max(ans, nums[l - 1] * nums[i] * nums[r + 1] + dfs(l, i - 1) + dfs(i + 1, r))
        return ans
    
    return dfs(1, len(nums) - 2)
    
def maxCoins_iterative(nums: List[int]) -> int:
    nums = [1] + nums + [1]
    n = len(nums)

    dp = [[0] * n for _ in range(n)]

    for l in range(n-2, 0, -1):
        for r in range(l, n-1):
            dp[l][r] = -float('inf')
            for i in range(l, r + 1):
                dp[l][r] = max(dp[l][r], nums[l - 1] * nums[i] * nums[r + 1] + dp[l][i - 1] + dp[i + 1][r])
    return dp[1][n-2]