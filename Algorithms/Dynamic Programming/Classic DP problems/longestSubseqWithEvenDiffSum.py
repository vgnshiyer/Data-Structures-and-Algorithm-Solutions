from functools import lru_cache

'''
Given an array, find the length of the longest subsequence such that the sum of differences between adjacent elements in the subsequence is even.
eg. [1,2,4,7] -> 4 (1,2,4,7)
    diff = [(2 - 1), (4 - 2), (7 - 4)] = [1,2,3]

    for subsequence [1, 2, 4, 7], sum of differences = 1 + 2 + 3 = 6 (even)
    therefore ans = 4
'''

@lru_cache(None)
def longestSubseq(i, p, s):
    if i >= len(arr): return 0 if s % 2 == 0 else -float('inf')

    include = 1 + longestSubseq(i + 1, arr[i], s + p - arr[i])
    exclude = longestSubseq(i + 1, p, s)
    return max(include, exclude)

def longestSubseq_iterative():
    dp = [[-float('inf')] * 2 for _ in range(len(arr))]
    dp[0][0] = 1

    for i in range(1, len(arr)):
        for j in range(i):
            diff = arr[i] - arr[j]
            if diff % 2 == 0:
                dp[i][0] = max(dp[i][0], dp[j][0] + 1)
                dp[i][1] = max(dp[i][1], dp[j][1] + 1)
            else:
                dp[i][0] = max(dp[i][0], dp[j][1] + 1)
                dp[i][1] = max(dp[i][1], dp[j][0] + 1)

    return dp[-1][0]

arr = [1,2,4,7]
print(longestSubseq(0, arr[0], 0))
print(longestSubseq_iterative())