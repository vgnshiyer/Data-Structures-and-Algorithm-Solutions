'''
Using the same minimax algorithm as used in stone game III.
This time we don't have any score to track. However, we can use 0 and 1 to make sure that the value remains positive for alice and remains negative for bob.
'''
def winnerSquareGame(self, n):
    '''
    The memoized solution fails with a TLE.
    '''
    @cache
    def minimax(n, max_player):
        if n == 0:
            return 0

        ans = float('-inf') if max_player else float('inf')
        if max_player:
            for i in range(1, int(n**0.5) + 1):
                ans = max(ans, 1 + minimax(n - i*i, False))
        else:
            for i in range(1, int(n**0.5) + 1):
                ans = min(ans, -1 + minimax(n - i*i, True))
        return ans

    ans = minimax(n, True)
    return ans > 0

def winnerSquareGame_iterative(n):
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        dp[i] = -float('inf')
        for j in range(1, int(i**0.5) + 1):
            if i >= j*j: dp[i] = max(dp[i], 1 - dp[i - j*j])
    return dp[n] > 0

'''
The above solution can be optimized by a minor tweak. Once we found a solution for alice to win from a particular state, there is no reason for us to keep looking in that path. We can simply break out of the loop.
'''
def winnerSquareGame(n):
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        dp[i] = -float('inf')
        for j in range(1, int(i**0.5) + 1):
            if i >= j*j: 
                dp[i] = max(dp[i], 1 - dp[i - j*j])
                if dp[i]: break ## <-- this is the optimization
    return dp[n] > 0