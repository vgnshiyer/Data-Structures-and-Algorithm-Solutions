def makeArrayIncreasing(arr1: List[int], arr2: List[int]) -> int:
    '''
    state: dp[i][m] -> min operations from index i given max so far is m
    transition: dp[i][m] = min(dp[i+1][max(cur, m)], 1 + dp[i+1][max(m, arr2[j])])
    base case: dp[len(arr1)][] = 0
    '''
    arr2.sort()

    def bs(target):
        l, r = 0, len(arr2)
        ans = -1
        while l < r:
            m = (l + r) >> 1
            if arr2[m] <= target: l = m + 1
            else: 
                ans = arr2[m]
                r = m
        return ans

    @cache
    def dfs(i, P):
        if i >= len(arr1): return 0
        
        ans = 10 ** 9
        if arr1[i] > P: ans = dfs(i + 1, arr1[i])
        nxt = bs(P)
        if nxt > P: 
            ans = min(ans, 1 + dfs(i + 1, nxt))
        return ans
    res = dfs(0, -1)
    return res if res != 10 ** 9 else -1