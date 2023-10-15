## recursive dp
def numWays(steps: int, arrLen: int) -> int:
  mod = 10 ** 9 + 7
  def dfs(i, j, dp):
      if i >= arrLen or i < 0: return 0
      if j == 0: return i == 0

      if (i, j) in dp: return dp[(i, j)]
      left = dfs(i - 1, j - 1, dp) % mod
      stay = dfs(i, j - 1, dp) % mod
      right = dfs(i + 1, j - 1, dp) % mod

      dp[(i, j)] = (left + stay + right) % mod
      return dp[(i, j)]

  return dfs(0, steps, {})
  
## recursive dp (Optimized)
def numWays(steps: int, arrLen: int) -> int:
  mod = 10 ** 9 + 7
  def dfs(i, j, dp):
      if i > j: return 0 ## Came too far -- no way to go back with the steps left
      if i >= arrLen or i < 0: return 0
      if j == 0: return i == 0

      if (i, j) in dp: return dp[(i, j)]
      left = dfs(i - 1, j - 1, dp) % mod
      stay = dfs(i, j - 1, dp) % mod
      right = dfs(i + 1, j - 1, dp) % mod

      dp[(i, j)] = (left + stay + right) % mod
      return dp[(i, j)]

  return dfs(0, steps, {}) 
  
## iterative dp
def numWays(steps: int, arrLen: int) -> int:
  mod = 10 ** 9 + 7

  dp = [[0] * arrLen for _ in range(steps + 1)]
  dp[0][0] = 1

  for j in range(1, steps + 1):
      for i in range(arrLen):
          if i > j: break
          left = (dp[j - 1][i - 1] if i else 0) % mod
          stay = (dp[j - 1][i]) % mod
          right = (dp[j - 1][i + 1] if i < arrLen - 1 else 0) % mod

          dp[j][i] = (left + stay + right) % mod
  return dp[steps][0]
  
## iterative dp -- space optimized
def numWays(self, steps: int, arrLen: int) -> int:
  mod = 10 ** 9 + 7

  dp = [0] * arrLen
  dp[0] = 1

  for j in range(1, steps + 1):
      dp_copy = dp.copy()
      for i in range(arrLen):
          if i > j: break
          left = (dp[i - 1] if i else 0) % mod
          stay = (dp[i]) % mod
          right = (dp[i + 1] if i < arrLen - 1 else 0) % mod

          dp_copy[i] = (left + stay + right) % mod
      dp = dp_copy
  return dp[0] 