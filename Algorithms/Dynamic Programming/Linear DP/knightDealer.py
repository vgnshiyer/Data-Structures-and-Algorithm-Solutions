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