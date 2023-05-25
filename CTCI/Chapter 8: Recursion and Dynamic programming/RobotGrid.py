## returns min distance path from source to dest

## without memoization
def findPath(grid: list, i: int, j: int, r: int, c: int) -> int:
    if i >= r or j >= c or grid[i][j] == '*':
        return r*c + 1
    if i == r-1 and j == c-1:
        return 1

    return 1 + min(findPath(grid, i + 1, j, r, c), findPath(grid, i, j + 1, r, c))

## with memoization
def findPathTopDown(grid: list, i: int, j: int, r: int, c: int, dp: list) -> int:
    if i >= r or j >= c or grid[i][j] == '*':
        return r*c + 1
    if i == r-1 and j == c-1:
        return 1

    if dp[i][j] == -1:
        dp[i][j] = 1 + min(findPathTopDown(grid, i + 1, j, r, c, dp), findPathTopDown(grid, i, j + 1, r, c, dp))

    return dp[i][j]

## iterative
def findPathBottomUp(grid: list) -> int:
    r, c = len(grid), len(grid[0])
    dp = [[0]*(c) for i in range(r)]

    for i in range(r): dp[i][0] = i+1
    for j in range(c): dp[0][j] = j+1

    for i in range(1, r):
        for j in range(1, c):
            dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
    return dp[r-1][c-1]

if __name__ == '__main__':
    grid = [
        '...*',
        '.*..',
        '....',
        '....'
    ]

    print(findPath(grid, 0, 0, 4, 4))

    dp = [[-1]*4 for i in range(4)]
    print(findPathTopDown(grid, 0, 0, 4, 4, dp))
    print(findPathBottomUp(grid))