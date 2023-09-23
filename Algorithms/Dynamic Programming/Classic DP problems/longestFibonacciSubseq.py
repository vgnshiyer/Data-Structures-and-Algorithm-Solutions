## DP + 2sum
def lenLongestFibSubseq(arr: List[int]) -> int:
    '''
    state: dp[r][i] -> longest fib sunseq ending with a[r], a[i]
    transition: dp[r][i] = dp[l][r] + 1 such that a[l] + a[r] == a[i]
    '''

    dp = [[0] * len(arr) for _ in range(len(arr))]

    best = 0
    for i in range(2, len(arr)):
        l, r = 0, i - 1
        while l < r:
            s = arr[l] + arr[r]
            if s < arr[i]: l += 1
            elif s > arr[i]: r -= 1
            else:
                dp[r][i] = 1 + dp[l][r]
                best = max(best, dp[r][i])
                r -= 1
                l += 1
    return best if not best else best + 2

## DP + hashmap
def lenLongestFibSubseq(arr):
    mp = {}  # mp[Value] = position
    n = len(arr)
    
    dp = [[0] * n for _ in range(n)]
    
    res = 0
    mp[arr[0]] = 0
    mp[arr[1]] = 1
    
    for i in range(2, n):
        mp[arr[i]] = i
        for j in range(i-1, 0, -1): ## doing the iteration like this instead of (1, i) allows us to stop when the difference becomes greater than arr[j]
            preVal = arr[i] - arr[j]
            # The last 3 numbers in the Fibonacci subsequence should be {preVal, arr[j], arr[i]}
            
            if preVal >= arr[j]: # eg. 7 - 2 = 5.. 5 could appear after 2 in the array which makes the subsequence invalid
                break
            
            # If the subsequence {..., preVal, arr[j]} was found
            if preVal in mp:
                # Extend the length by 1, and the tail is {..., arr[j], arr[i]} now
                dp[j][i] = dp[mp[preVal]][j] + 1
                res = max(res, dp[j][i])
    
    # res + 2: We haven't put the first two numbers in the result
    return res + 2 if res else 0
