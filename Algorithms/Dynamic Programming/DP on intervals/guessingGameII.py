'''
We try all guesses in a range. We traverse left range and the right range to get the worst possible cost from both. At the same time we maintain the minimum maximum amount we need to guarantee a win in this game of guessing.
'''

def getMoneyAmount(n: int) -> int:
  dp = {}
  def dfs(l, r):
      if l >= r: return 0

      if (l, r) in dp: return dp[(l, r)]

      maxPay = float('inf')
      for guess in range(l, r + 1):
          maxPay = min(maxPay, guess + max(dfs(l, guess - 1), dfs(guess + 1, r)))
      dp[(l, r)] = maxPay
      return maxPay

  return dfs(1, n)
  
def getMoneyAmount_iterative(n: int) -> int:
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for l in range(n, 0, -1):
        for r in range(l + 1, n + 1):
            dp[l][r] = float('inf')
            for guess in range(l, r + 1):
                left_max = dp[l][guess - 1] if (guess - 1) > l else 0
                right_max = dp[guess + 1][r] if (guess + 1) < r else 0
                dp[l][r] = min(dp[l][r], guess + max(left_max, right_max))
    return dp[1][n] 