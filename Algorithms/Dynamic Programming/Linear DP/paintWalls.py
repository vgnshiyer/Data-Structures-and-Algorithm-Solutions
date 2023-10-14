'''
State: dp[i][j] --> min cost to paint walls till index i. given the current wait time is j
transition: dp[i][j] = min(dp[i + 1][j - 1], dp[i + 1][j + time[i]]) ## either choose a free painter or select a paid painter

We check the total wait time at the end of array to check if we had a positive sum / 0 for the wait time

** It is better to have the dp passed as a parameter. Otherwise if kept outside, it gives a memory limit exceeded.
'''
def paintWalls(self, cost: List[int], time: List[int]) -> int:
    def dfs(i, ttw, dp):
        if i < 0: 
            return 0 if ttw >= 0 else float('inf')

        if (i, ttw) in dp: return dp[(i, ttw)]

        useCur = cost[i] + dfs(i - 1, ttw + time[i], dp)
        skipCur = dfs(i - 1, ttw - 1, dp)
        dp[(i, ttw)] = min(skipCur, useCur)

        return dp[(i, ttw)]

    return dfs(len(cost) - 1, 0, {})