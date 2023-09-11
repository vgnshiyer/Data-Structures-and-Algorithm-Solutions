from functools import cache

def mincostTickets(days: List[int], cost: List[int]) -> int:
    ## recursive solution
    @cache
    def helper(i, pass_expires_on):
        if i >= len(days): return 0
        if pass_expires_on >= days[-1]: return 0
        if days[i] <= pass_expires_on: return helper(i+1, pass_expires_on)

        return min([cost[0] + helper(i+1, days[i]), cost[1] + helper(i+1, days[i] + 6), cost[2] + helper(i+1, days[i] + 29)])

    # return helper(0, 0)

    ## iterative solution
    last_day = days[-1]
    dp = [0]*(last_day + 1)
    days = set(days)

    for i in range(1, last_day + 1):
        if i not in days: dp[i] = dp[i-1]
        else: dp[i] = min([cost[0] + dp[i-1], cost[1] + dp[max(0, i-7)], cost[2] + dp[max(0, i-30)]])

    return dp[-1]