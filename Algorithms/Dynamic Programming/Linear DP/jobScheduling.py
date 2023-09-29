def jobScheduling(startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    '''
    Question: Why does binary search work? If we select the nearest end time, why does it work? Arent we ignoring a possible greater profit that can be made if the nearest element is not chosen?
    -> Look closely. At every index that we arrive, we are making a choice of either including that element or ignoring that element from our schedule. Therefore we do not need to worry about a possibly higher profit. 
    '''
    intervals = sorted(zip(startTime, endTime, profit))

    @cache
    def dfs(i):
        if i >= len(intervals): return 0

        start, end, pft = intervals[i]
        
        l, r = i+1, len(intervals)
        while l < r:
            m = (l + r) >> 1
            if intervals[m][0] < end: l = m + 1
            else: r = m
        
        return max(dfs(i+1), pft + dfs(r))

    return dfs(0)

def jobScheduling_iterative(startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    '''
    state: dp[i] -> max profit at this index
    transition: dp[i] = max(dp[i+1], pft + dp[r]) where r is the index of the nearest element that has a start time greater than or equal to the end time of the current element
    base case: dp[i] = 0
    '''
    intervals = sorted(zip(startTime, endTime, profit))
    dp = [0] * (len(intervals) + 1)

    for i in range(len(intervals) - 1, -1, -1):
        start, end, pft = intervals[i]

        l, r = i + 1, len(intervals)
        while l < r:
            m = (l + r) >> 1
            if intervals[m][0] < end: l = m + 1
            else: r = m
        dp[i] = max(dp[i+1], pft + dp[r]) ## since we are only checking the closest interal (as opposed to all possible ones like LCS), we are tracking the best value by doing dp[i] = max(dp[i + 1], ...)
    return dp[0]