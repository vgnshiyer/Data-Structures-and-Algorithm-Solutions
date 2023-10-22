'''
Intuition: We can have two variables tracking the start and end of the stick and have another two variables tracking the start and end of a cuts array.

We traverse the available cuts in the range and select the one which gives the minimum cost.

But this approach will have too many states to handle. To handle this problem, we just add 0 and n to our cuts array. 

That way we can easily get the current length of the stick and also track the range of cuts we need to visit for the current stick.

state: dp[i][j] -> minimum cost to cut the stick at end points i and j in the cuts array. cuts[i] and cuts[j] give the endpoints of the actual stick.

transition: dp[i][j] = min(dp[i][j], cuts[j] - cuts[i] + dp[i][k] + dp[k][j]) .. for k in range(i+1, j)

base case: dp[i][j] = 0 for j - i <= 1 # because there are not many available cuts between j and i
'''

def minCost_recursive(n: int, cuts: List[int]) -> int:
    cuts.extend([0, n])
    cuts.sort()

    def dfs(i, j, dp):
        if j - i <= 1: return 0 # not enough cuts available

        if (i, j) not in dp:
            ans = inf
            for k in range(i + 1, j):
                ans = min(ans, cuts[j] - cuts[i] + dfs(i, k, dp) + dfs(k, j, dp))
            dp[(i, j)] = ans

        return dp[(i, j)]

    return dfs(0, len(cuts) - 1, {})
    

def minCost_iterative(n: int, cuts: List[int]) -> int:
    cuts.extend([0, n])
    cuts.sort()
    N = len(cuts)

    dp = [[0] * N for _ in range(N)]

    for i in range(N - 1, -1, -1):
        for j in range(i + 2, N):
            dp[i][j] = inf
            for k in range(i + 1, j):
                dp[i][j] = min(dp[i][j], cuts[j] - cuts[i] + dp[i][k] + dp[k][j])
    return dp[i][j] 