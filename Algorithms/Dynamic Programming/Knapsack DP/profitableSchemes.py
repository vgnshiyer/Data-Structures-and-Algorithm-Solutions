'''
- Look at the constraints carefully.
- Simply by limiting the pft in the state to 102 removed the memory limit exceeded error.
- Without that, the profit can be boundless, which means we would be storing a lot of unncecessary states.
- All we need to know is, if the profit is reaching minProfit or not.
'''
def profitableSchemes(n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
    mod = 10 ** 9 + 7
    dp = [[[-1] * 102 for _ in range(102)] for _ in range(102)]

    def findNumSchemes(i=0, members=0, pft=0):
        if i >= len(profit): return 0

        if dp[i][members][pft] != -1: return dp[i][members][pft]

        ## take current scheme
        ans = pft + profit[i] >= minProfit and members + group[i] <= n
        if members + group[i] <= n:
            ans += findNumSchemes(i + 1, members + group[i], min(minProfit, pft + profit[i]))

        ## ignore current scheme
        ans += findNumSchemes(i + 1, members, pft)
        dp[i][members][pft] = ans % mod
        return dp[i][members][pft]
    
    numSchemes = findNumSchemes() % mod 
    return numSchemes if minProfit > 0 else numSchemes + 1 ## one way to get zero profit is to choose no schemes

## Alternative memoized solution
'''
- Notice that here we only increment the answer when we reach the end of the profit array.
- This approach is much better than the previous one where we were incrementing in every recursive call whenever we found a pft greater than minProfit.
- Always try to increment the counter at the final state instead of anywhere else. It causes discrepenacies to the final answer.
'''
def profitableSchemes2(n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
    mod = 10 ** 9 + 7
    dp = [[[-1] * 102 for _ in range(102)] for _ in range(102)]

    def findNumSchemes(i=0, members=0, pft=0):
        if i >= len(profit):
            if pft >= minProfit and members <= n: return 1
            return 0
        if members > n: return 0
        
        if dp[i][members][pft] != -1: return dp[i][members][pft]

        ## take current scheme
        use = findNumSchemes(i + 1, members + group[i], min(minProfit, pft + profit[i]))

        ## ignore current scheme
        ignore = findNumSchemes(i + 1, members, pft)
        
        dp[i][members][pft] = (use % mod + ignore % mod) % mod
        return dp[i][members][pft]

    return findNumSchemes() % mod

def profitableSchemes_iterative(n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
    mod = 10 ** 9 + 7
    dp = [[[0] * 102 for _ in range(102)] for _ in range(102)]
    
    dp[len(profit)][n][minProfit] = 1

    for i in range(len(profit) - 1, -1, -1):
        for j in range(n, -1, -1):
            for k in range(minProfit, -1, -1):
                dp[i][j][k] = dp[i + 1][j][k]
                if j + group[i] <= n: 
                    dp[i][j][k] = (dp[i][j][k] + dp[i + 1][j + group[i]][min(minProfit, k + profit[i])]) % mod
    ans = 0
    for i in range(n + 1):
        ans = (ans + dp[0][i][0]) % mod ## all groups within the range of max members are valid
    return ans

## https://www.youtube.com/watch?v=MosNqLOkJ3Y
'''
Trick to reduce one dimension from the dp if to go bottom to top for j and k.
Going from left to right, will overwrite the previous value.

3D array is actually multiple snapshots of a 2D aray.

In multi dimensional dp, it doesnt really matter which direction you iterate in the inner loop. 
Keep in mind however, instead of i - 1, if we were doing dp[i][j-g], then we would have to create a copy of the dp. Since we are referring from the current snapshot.
'''
def profitableSchemes_spaceOptimized(n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
    mod = 10 ** 9 + 7
    dp = [[0] * 102 for _ in range(102)]
    
    dp[0][0] = 1

    for i in range(1, len(profit) + 1):
        for j in range(n, -1, -1):
            for k in range(minProfit, -1, -1):
                if j >= group[i-1]:
                    dp[j][k] = (dp[j][k] + dp[j - group[i-1]][max(0, k - profit[i-1])]) % mod
    ans = 0
    for i in range(n + 1):
        ans = (ans + dp[i][minProfit]) % mod
    return ans