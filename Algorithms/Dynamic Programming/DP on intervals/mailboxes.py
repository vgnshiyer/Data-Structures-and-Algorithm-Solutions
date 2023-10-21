'''
It is difficult to get the intuition for this problem. We think about dividing the houses based on the amount of mailboxes we can place. 

Case 1: K = 1 -> We have only one mailbox
Best place to place this mailbox in the median house of the range

Case 2: We have K = n mailboxes.
Best way to place them is to let each house have their own mailbox. Ans = 0.

Case 3: We Travel through the range of houses from left to right, and try placing 1 mailbox at every house. We calculate the cost 
        a. for dp(i, x, k) {Best way to place 1 mailbox in the range i,x}
        b. for dp(x + 1, k) {Best way to place the remaining k - 1 mailboxes in range x + 1, j}  
'''

def minDistance_recursive(houses: List[int], k: int) -> int:
    houses.sort()

    @cache
    def dfs(i, j, k):
        if k == 1:
            m = (i + j) >> 1
            ans = 0
            for x in range(i, j + 1):
                ans += abs(houses[x] - houses[m])
            return ans

        if k == j - i + 1: return 0

        if k > j - i + 1: return float('inf')

        ans = float('inf')
        for x in range(i, j):
            ans = min(ans, dfs(i, x, 1) + dfs(x + 1, j, k - 1))
        
        return ans

    return dfs(0, len(houses) - 1, k)
    

def minDistance_iterative(houses: List[int], k: int) -> int:
    n = len(houses)
    houses.sort()

    dp = [[[float('inf')] * (k + 1) for _ in range(n)] for _ in range(n)]

    for k in range(1, k + 1):
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if j - i + 1 < k: 
                    dp[i][j][k] = float('inf')
                    continue

                if k == 1: 
                    m = (j + i) >> 1
                    ans = 0
                    for x in range(i, j + 1):
                        ans += abs(houses[x] - houses[m])
                    dp[i][j][k] = ans
                    continue

                if k == j - i + 1:
                    dp[i][j][k] = 0
                    continue

                for x in range(i, j):
                    dp[i][j][k] = min(dp[i][j][k], 
                        dp[i][x][1] + dp[x + 1][j][k - 1])

    return dp[0][n - 1][k] 