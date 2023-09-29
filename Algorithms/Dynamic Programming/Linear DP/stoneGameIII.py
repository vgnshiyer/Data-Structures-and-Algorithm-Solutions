'''
Minimax algorithm: https://en.wikipedia.org/wiki/Minimax
It is decision rule algorithm used for minimizing the possible loss for a worst case scenario. It is formulated for zero sum game theory problems. Minmax it is the largest value the player can be sure to get when they know the actions of the other players. In other words, it is the worst case scenario for the player.

In the minMax algorithm, we maintain a variable maximizingPlayer which denotes whether the current player is maximizing or not. If the current player is maximizing, we return the maximum of the values returned by the recursive calls, otherwise we return the minimum of the values returned by the recursive calls.

At the top position, we get the maximum difference between the scores of the two players. If the difference is positive, it means that the first player is the winner, otherwise the second player is the winner. If the difference is 0, it means that the game is a tie.
'''

def stoneGameIII(stones: List[int]) -> str:
    n = len(stones)
    dp = [[-1] * 2 for _ in range(n + 1)]
    
    def minimax(i, maxPlayer):
        if i >= n: return 0

        if dp[i][maxPlayer] != -1: return dp[i][maxPlayer]

        score = 0
        ans = 0
        if maxPlayer:
            ans = -float('inf')
            for k in range(i, min(n, i + 3)):
                score += stones[k]
                ans = max(ans, score + minimax(k + 1, 0))
        else:
            ans = float('inf')
            for k in range(i, min(n, i + 3)):
                score += stones[k]
                ans = min(ans, -score + minimax(k + 1, 1))
        dp[i][maxPlayer] = ans
        return ans

    ans = minimax(0, 1)
    if ans > 0: return 'Alice'
    elif ans < 0: return 'Bob'
    return 'Tie'

## iterative version
def stoneGameIII_iterative(stones: List[int]) -> str:
    n = len(stones)
    dp = [[-1] * 2 for _ in range(n + 1)]
    dp[-1] = [0, 0]

    for i in range(n - 1, -1, -1):
        dp[i][1] = -float('inf')
        dp[i][0] = float('inf')

        score = 0
        for k in range(i, min(n, i + 3)):
            score += stones[k]
            dp[i][1] = max(dp[i][1], score + dp[k + 1][0])
            dp[i][0] = min(dp[i][0], -score + dp[k + 1][1])

    ans = dp[0][1]       
    if ans > 0: return 'Alice'
    elif ans < 0: return 'Bob'
    return 'Tie'

## Space Optimized - eliminate a state
def stoneGameIII(stones: List[int]) -> str:
    n = len(stones)
    dp = [-1 for _ in range(n + 1)]
    dp[-1] = 0

    for i in range(n - 1, -1, -1):
        dp[i] = -float('inf')

        score = 0
        for k in range(i, min(n, i + 3)):
            score += stones[k]
            dp[i] = max(dp[i], score - dp[k + 1])

    ans = dp[0]
    if ans > 0: return 'Alice'
    elif ans < 0: return 'Bob'
    return 'Tie'