def findBall(grid: List[List[int]]) -> List[int]:
    n, m = len(grid), len(grid[0])
    
    @cache
    def trace(i, j):
        if j < 0 or j >= m: return -1
        if i >= n: return j
        
        isRight = grid[i][j] == 1
        isLeft = grid[i][j] == -1

        isV = (j < m - 1 and (isRight and grid[i][j + 1] == -1)) or (j > 0 and (isLeft and grid[i][j - 1] == 1))
        if isV: return -1
        return trace(i + 1, j + 1) if isRight else trace(i + 1, j - 1)

    answer = [-1] * m
    for i in range(m):
        answer[i] = trace(0, i)
    return answer

def findBall_iterative(grid: List[List[int]]) -> List[int]:
    n, m = len(grid), len(grid[0])

    dp = [[-1] * (m + 1) for _ in range(n + 1)]
    for i in range(m): dp[-1][i] = i

    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if j < m - 1 and (grid[i][j] == 1 and grid[i][j + 1] == -1): continue
            if j > 0 and (grid[i][j] == -1 and grid[i][j - 1] == 1): continue
            dp[i][j] = dp[i + 1][j + 1] if grid[i][j] == 1 else (dp[i + 1][j - 1] if j else -1)
    return dp[0][:-1]