'''
Maximum coins according to the constraints is 1000. 
op1: coins[i] - k
op2: coins[i] // 2 -> for all children

Since max coin is 1000, after 13 divisions, there will be no coins left <- our base case

State: dp[i][v] -> max number of coins at node at with v number of divisions (bit shift)
Transition: dp[i][v] = max(coins[i] - k + dp[j][v], coins[i] >> v + 1 + dp[j][v + 1])
'''
def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
  dp = {}
  
  def dfs(i, p, v):
      if v > 13: return 0 # no coins left
      if (i, v) in dp: return dp[(i, v)]

      op1 = (coins[i] >> v) - k
      op2 = coins[i] >> v + 1
      for j in adj[i]:
          if j == p: continue
          op1 += dfs(j, i, v)
          op2 += dfs(j, i, v + 1)
      dp[(i, v)] = max(op1, op2)
      return dp[(i, v)]

  adj = defaultdict(list)
  for x, y in edges:
      adj[x].append(y)
      adj[y].append(x)

  return dfs(0, -1, 0)