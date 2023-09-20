'''
Mistakes I made:
- returned result as soon as found, without checking for better possible solutions by moving forward in either of the strings
- was returning max(dp[i+1][j], dp[i][j+1]). This would make the algorithm find the longest subsequence instead of substring.
- in case of substring, you either include the element, or start a new substring. (start from 0) return 0
'''
def findLength(nums1: List[int], nums2: List[int]) -> int:
    ans = 0
    @cache
    def dfs(i, j):
        nonlocal ans
        if i >= len(nums1) or j >= len(nums2): return 0

        res = 0
        if nums1[i] == nums2[j]: 
            res = 1 + dfs(i + 1, j + 1)
            ans = max(ans, res)
        dfs(i + 1, j)
        dfs(i, j + 1)
        return res

    dfs(0, 0)
    return ans

def findLength_iterative(nums1: List[int], nums2: List[int]) -> int:
    ans = 0
    n, m = len(nums1), len(nums2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if nums1[i - 1] == nums2[j - 1]: dp[i][j] = 1 + dp[i - 1][j - 1]
            ans = max(ans, dp[i][j])
    return ans

def findLength_iterative_spaceOptimized(nums1, nums2):
    ans = 0
    n, m = len(nums1), len(nums2)

    dp = [0] * (m + 1)

    for i in range(1, n + 1):
        dp2 = [0] * (m + 1)
        for j in range(1, m + 1):
            if nums1[i - 1] == nums2[j - 1]: dp2[j] = 1 + dp[j - 1]
            ans = max(ans, dp2[j])
        dp = dp2
    return ans

## solution using Knuth-Morris-Patt search
def findLength_kmp(nums1: List[int], nums2: List[int]) -> int:
    n, m = len(nums1), len(nums2)
    
    def computeLps(nums) -> list:
        m = len(nums)
        j = 0
        lps = [0] * m

        for i in range(1, m):
            while j > 0 and nums[i] != nums[j]: j = lps[j - 1]
            if nums[i] == nums[j]: 
                j += 1
                lps[i] = j
        return lps

    '''
    Notice that we are checking the pattern from every possible index. 
    from 0 - n-1, 1 - n-1, 2 - n-1, ... and so on.
    We take record of the maximum common prefix at every step.
    '''
    ans = 0
    while len(nums2):
        lps = computeLps(nums2)
        j = 0
        for i in range(n):
            while j > 0 and nums1[i] != nums2[j]: j = lps[j - 1]
            if nums1[i] == nums2[j]: j += 1
            ans = max(ans, j)
            if j == len(nums2): break
        del[nums2[0]]
    return ans