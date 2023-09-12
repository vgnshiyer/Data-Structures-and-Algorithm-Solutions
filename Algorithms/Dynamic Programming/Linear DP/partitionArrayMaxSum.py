def maxSumAfterPartitioning(arr: List[int], k: int) -> int:
    '''
    state: dp[i] -> max sum after partitioning at index i
    transition: dp[i] = max(dp[i], dp[i-j] + max(arr[i-j:i+1]) * j) for j in range(1, k+1)
    base case: dp[0] = arr[0]
    '''
    @cache
    def helper(start):
        if start >= len(arr): return 0
        mx = 0
        ans = 0
        for i in range(start, start + k):
            if i >= len(arr): break
            mx = max(mx, arr[i])
            leftPartitionSum = mx * (i - start + 1)
            rightPartitionSum = helper(i+1)
            ans = max(ans, leftPartitionSum + rightPartitionSum)
        return ans
    return helper(0)

def maxSumAfterPartitioning_iterative(arr: List[int], k: int) -> int:
    dp = [0] * (len(arr) + 1)
    
    for i in range(len(arr)-1, -1, -1):
        mx = 0
        ans = 0
        for j in range(i, i + k):
            if j >= len(arr): break
            mx = max(mx, arr[j])
            leftPartitionSum = mx * (j - i + 1)
            rightPartitionSum = dp[j+1]
            ans = max(ans, leftPartitionSum + rightPartitionSum)
        dp[i] = ans 
    return dp[0]