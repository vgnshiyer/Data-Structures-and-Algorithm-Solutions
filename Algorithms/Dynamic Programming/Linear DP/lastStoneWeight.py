'''
This problem is similar to partition equal subset sum. It was difficult to notice the pattern. 
'''
def lastStoneWeightII(self, stones: List[int]) -> int:
    '''
    Divide the stones into 2 partitions with sums 
    S1 + S2 = S --> (1)
    We need to maximize the difference between the sums
    S2 - S1 = d --> (2)

    Add (1) & (2)

    d = S - 2*S2 --> max value for d is the answer
    '''

    n, S = len(stones), sum(stones)
    dp = [[0] * (S + 1) for _ in range(n + 1)]
    for i in range(n + 1): dp[i][0] = 1

    # we capture all possible sums in the knapsack
    for i in range(1, n + 1):
        for j in range(1, S + 1): # mistake: starting from stones[i-1] instead of 1 --> this can only be done when we have a 1D array for our dp as it retains the previous state for (i - 1)
            dp[i][j] = dp[i - 1][j] # ignore the current stone
            if stones[i - 1] > j: continue
            dp[i][j] |= dp[i - 1][j - stones[i - 1]] # include the current stone in the knapsack
        # the boolean array tracks all the possible sums  
    
    # We track all possible sums but only consider (0, S/2) according to our formula
    for i in range((S // 2), -1, -1):
        if dp[n][i]: return S - 2 * i
        
'''
Approach 2: We maintain two knapsacks -> one for positive sum and one for negative sum
We store the difference of the two sums. If the difference is greater than or equal to 0 we return the minimum value
Notice that our difference can be negative. -> we offset it with 3000. (max input value for sum)
'''
def lastStoneWeightII(self, stones: List[int]) -> int:
    dp = [[-1] * 6001 for _ in range(31)]

    # min stone if with stone i and running sum j
    def epicSmash(i, j):
        if i >= len(stones):
            return j if j >= 0 else float('inf')

        if dp[i][j + 3000] != -1: return dp[i][j + 3000]

        ans = min(epicSmash(i + 1, j - stones[i]), epicSmash(i + 1, j + stones[i]))
        dp[i][j + 3000] = ans
        return ans

    return epicSmash(0, 0)
    
'''Iterative''' 
def lastStoneWeightII(self, stones: List[int]) -> int:
    dp = {0}

    n = len(stones)
    for i in range(n):
        dp2 = set()
        for j in dp:
            dp2.add(j - stones[i])
            dp2.add(j + stones[i])
        dp = dp2

    minStones = float('inf')
    for stone in dp: 
        minStones = min(minStones, abs(stone))
    return minStones