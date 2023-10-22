def combinationSum4(nums: List[int], target: int) -> int:
  @cache
  def dfs(i, t):
      if t < 0: return 0
      if t == 0: return 1
      if i >= len(nums): return 0

      ans = 0
      for k in range(i, len(nums)):
          ans += dfs(i, t - nums[k])
      return ans

  return dfs(0, target)
  
  
def combinationSum4_iterative(nums: List[int], target: int) -> int:
    dp = [0] * (target + 1)
    dp[0] = 1

    for j in range(1, target + 1):
        for n in nums:
            if n <= j: dp[j] += dp[j - n]
    return dp[target] 