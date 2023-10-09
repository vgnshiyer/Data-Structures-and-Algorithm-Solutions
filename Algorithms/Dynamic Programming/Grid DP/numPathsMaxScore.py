def pathsWithMaxScore(board: List[str]) -> List[int]:
    n, m = len(board), len(board[0])
    mod = 10 ** 9 + 7

    score = [[-float('inf')] * (m + 1) for _ in range(n + 1)]
    paths = [[0] * (m + 1) for _ in range(n + 1)]
    paths[1][1] = 1

    for i in range(n):
        for j in range(m):
            if board[i][j] in 'ES': score[i + 1][j + 1] = 0
            elif board[i][j] == 'X': score[i + 1][j + 1] = -float('inf')
            else: score[i + 1][j + 1] = int(board[i][j])

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1: continue

            top = score[i - 1][j]
            left = score[i][j - 1]
            diag = score[i - 1][j - 1]

            maxScore = max([top, left, diag])
            numPaths = 0

            if top == maxScore: numPaths = (numPaths + paths[i - 1][j]) % mod
            if left == maxScore: numPaths = (numPaths + paths[i][j - 1]) % mod
            if diag == maxScore: numPaths = (numPaths + paths[i - 1][j - 1]) % mod

            score[i][j] += maxScore
            paths[i][j] = numPaths % mod
    
    maxScore, numPaths = score[n][m], paths[n][m]
    if maxScore == -float('inf'): maxScore, numPaths = 0, 0

    return [maxScore, numPaths]