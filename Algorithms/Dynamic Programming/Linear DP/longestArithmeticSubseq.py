def longestSubsequence(self, arr: List[int], difference: int) -> int:
    '''
    state: dp[i] -> longest AP at this index
    transition: dp[i] = max(dp[i], dp[j] + 1) if arr[i] - arr[j] == d (we store previous elements in a hashmap -> if ele - diff is found simply add 1)
    base case: dp[i] = 1
    '''
    dp = [1] * len(arr)
    longestSubseq = 1
    hashMap = {}
    for i in range(len(arr)):
        if arr[i] - difference in hashMap:
            j = hashMap[arr[i] - difference]
            dp[i] = 1 + dp[j]
        hashMap[arr[i]] = i
        longestSubseq = max(longestSubseq, dp[i])
    return longestSubseq