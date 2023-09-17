def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
    '''
    state: dp[i][j] -> min RLE string starting at index i with at most j removals
    transition: dp[i][j] = min(dp[i+1][j+1], 1 + (cnt) + dp[i+1][j])
    base case: dp[len(s)][j] = 0
                dp[i][<k] = inf --> at most k deletions
    '''
    memo = {}

    @cache
    def dfs(i, j, prev, prev_cnt):
        if i >= len(s): return 0
        if j > k: return float('inf')

        ## delete current element
        delete = dfs(i + 1, j + 1, prev, prev_cnt)

        ## keep this element
        if s[i] == prev:
            keep = dfs(i + 1, j, s[i], prev_cnt + 1)

            if prev_cnt in [1, 9, 99]: keep += 1
        else:
            keep = 1 + dfs(i + 1, j, s[i], 1)
        
        return min(keep, delete)

    return dfs(0, 0, '*', 0)