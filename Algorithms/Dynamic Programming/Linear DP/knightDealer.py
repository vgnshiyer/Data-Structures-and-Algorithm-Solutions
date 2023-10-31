def knightDialer(n: int) -> int:
    mod = 10 ** 9 + 7
    knightMoves = [(-1, -2), (1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1)]

    dp = [[[0] * (n + 1) for _ in range(3)] for _ in range(4)]

    for i in range(4):
        for j in range(3):
            if i == 3 and j != 1: continue
            dp[i][j][1] = 1

    for k in range(2, n + 1):
        for i in range(4):
            for j in range(3):
                if i == 3 and j != 1: continue
                for nextMove in knightMoves:
                    x, y = nextMove
                    dx, dy = i + x, j + y
                    if dx < 0 or dx >= 4 or dy < 0 or dy >= 3 or (dx == 3 and dy != 1): continue
                    dp[i][j][k] = (dp[i][j][k] + dp[dx][dy][k-1]) % mod

    num_distinct_phone_numbers = 0
    for i in range(4):
        for j in range(3):
            num_distinct_phone_numbers = (num_distinct_phone_numbers + dp[i][j][n]) % mod

    return num_distinct_phone_numbers

# optimized graph solution
def knightDialer(n: int) -> int:
    adj = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [4, 2]]
    mod = 10 ** 9 + 7

    dp = [[0] * (n) for _ in range(10)]
    for i in range(10): dp[i][0] = 1

    for j in range(1, n):
        for i in range(10):
            dp[i][j] = 0
            for k in adj[i]:
                dp[i][j] += dp[k][j - 1]
                dp[i][j] %= mod
    
    total = 0
    for i in range(10): 
        total += dp[i][n - 1]
        total %= mod
    return total