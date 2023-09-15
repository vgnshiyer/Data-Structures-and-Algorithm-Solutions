def stoneGameIII(stoneValue: List[int]) -> str:
    '''
    We need to maximize the score difference between alice and bob. Think about finding the 
    state: dp[i] -> max score at score difference at i provided that the other person plays optimally
    transition: dp[i] = max(dp[i], score_so_far - dp[j + 1])
    '''

    n = len(stoneValue)
    dp = [0] * (n + 1)
    
    for i in range(n-1, -1, -1):
        score_so_far = 0
        dp[i] = -float('inf')
        for j in range(i, min(n, i + 3)):
            score_so_far += stoneValue[j]
            dp[i] = max(dp[i], score_so_far - dp[j+1])

    if dp[0] > 0: return 'Alice'
    if dp[0] < 0: return 'Bob'
    return 'Tie'

'''
Minimax algorithm: https://en.wikipedia.org/wiki/Minimax
It is decision rule algorithm used for minimizing the possible loss for a worst case scenario. It is formulated for zero sum game theory problems. Minmax it is the largest value the player can be sure to get when they know the actions of the other players. In other words, it is the worst case scenario for the player.

In the minMax algorithm, we maintain a variable maximizingPlayer which denotes whether the current player is maximizing or not. If the current player is maximizing, we return the maximum of the values returned by the recursive calls, otherwise we return the minimum of the values returned by the recursive calls.

At the top position, we get the maximum difference between the scores of the two players. If the difference is positive, it means that the first player is the winner, otherwise the second player is the winner. If the difference is 0, it means that the game is a tie.
'''

def stoneGameIII_minimax(stoneValue: List[int]) -> str:
    n = len(stoneValue)

    @cache
    def minimax(i, maximizingPlayer):
        if i >= len(stoneValue): return 0

        ans = float('inf') if maximizingPlayer == 0 else -float('inf')
        score = 0
        for j in range(i, min(n, i + 3)):
            if maximizingPlayer == 1:
                score += stoneValue[j]
                ans = max(ans, score + minimax(j+1, 0))
            else:
                score -= stoneValue[j]
                ans = min(ans, score + minimax(j+1, 1))
        return ans

    ans = minimax(0, 1)
    if ans > 0: return 'Alice'
    if ans < 0: return 'Bob'
    return 'Tie'

## iterative version
def stoneGameIII_iterative(stoneValue: List[int]) -> str:
    n = len(stoneValue)

    dp = [[float('inf'), -float('inf')] for _ in range(n+1)]
    dp[-1] = [0, 0]

    for i in range(n-1, -1, -1):
        s1 = s2 = 0
        for j in range(i, min(n, i + 3)):
            s1 += stoneValue[j]
            dp[i][1] = max(dp[i][1], s1 + dp[j+1][0])

            s2 -= stoneValue[j]
            dp[i][0] = min(dp[i][0], s2 + dp[j+1][1])

    ans = dp[0][1]
    if ans > 0: return 'Alice'
    if ans < 0: return 'Bob'
    return 'Tie'