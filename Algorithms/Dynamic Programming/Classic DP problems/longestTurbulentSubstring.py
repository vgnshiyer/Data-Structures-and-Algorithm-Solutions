def maxTurbulenceSize(arr: List[int]) -> int:
    '''
    if i is even, 
    arr[i] < arr[i-1]
    else
    arr[i] > arr[i-1]

    or the other way round

    state: dp[i][0] -> longest turbulent substring ending at i, even positions are smaller
            dp[i][1] -> longest turbulent substring ending at i, odd positions are smaller
    transition: dp[i][0] = 1 + dp[i-1][0] if i & 1 and a[i] > a[i-1] or i & 1 == 0 and a[i] < ar[i-1]
                dp[i][1] = 1 + dp[i-1][1] if i & 1 and a[i] < a[i-1] or i & 1 == 0 and a[i] > a[i-1]

    base case: dp[i][0] = dp[i][1] = 1
    '''

    n = len(arr)
    dp = [[1] * 2 for _ in range(n)]
    ans = 1

    for i in range(1, n):
        if i & 1:
            if arr[i] > arr[i-1]: dp[i][0] = 1 + dp[i-1][0]
            elif arr[i] < arr[i-1]: dp[i][1] = 1 + dp[i-1][1]
        else:
            if arr[i] < arr[i-1]: dp[i][0] = 1 + dp[i-1][0]
            elif arr[i] > arr[i-1]: dp[i][1] = 1 + dp[i-1][1]
        ans = max(ans, max(dp[i]))
    return ans

    def maxTurbulenceSize_spaceOptimized(arr: List[int]) -> int:
        n = len(arr)
        lts1 = lts0 = 1
        ans = 1
        for i in range(1, n):
            if i & 1:
                if arr[i] > arr[i-1]: 
                    lts0 = 1 + lts0
                    lts1 = 1
                elif arr[i] < arr[i-1]: 
                    lts1 = 1 + lts1
                    lts0 = 1
                else: lts0 = lts1 = 1
            else:
                if arr[i] < arr[i-1]: 
                    lts0 = 1 + lts0
                    lts1 = 1
                elif arr[i] > arr[i-1]: 
                    lts1 = 1 + lts1
                    lts0 = 1
                else: lts0 = lts1 = 1
            ans = max(ans, max(lts0, lts1))
        return ans