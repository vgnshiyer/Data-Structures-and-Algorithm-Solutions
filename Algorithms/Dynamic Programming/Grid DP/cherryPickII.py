def cherryPickup(grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])

    @cache
    def getMaxCherries(r1, c1, r2, c2):
        if r1 == n and r2 == n: return 0
        if r1 >= n or r2 >= n or c1 < 0 or c1 >= m or c2 < 0 or c2 >= m: return -float('inf')

        restMaxCherries = -float('inf')
        for r11, c11, r21, c21 in [(1, 0, 1, 0), (1, 0, 1, 1), (1, 1, 1, 0), (1, 1, 1, 1), (1, 0, 1, -1), (1, -1, 1, 0), (1, -1, 1, -1), (1, -1, 1, 1), (1, 1, 1, -1)]:
            restMaxCherries = max(restMaxCherries, getMaxCherries(r1 + r11, c1 + c11, r2 + r21, c2 + c21))
        if r1 == r2 and c1 == c2: return grid[r1][c1] + restMaxCherries
        return grid[r1][c1] + grid[r2][c2] + restMaxCherries

    return getMaxCherries(0, 0, 0, m - 1)

def cherryPickup_spaceOptimized(grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])

    @cache
    def getMaxCherries(r, c1, c2):
        if r == n: return 0
        if c1 < 0 or c1 >= m or c2 < 0 or c2 >= m: return -float('inf')

        restMaxCherries = -float('inf')
        for c11, c21 in [(0, 0), (0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1)]:
            restMaxCherries = max(restMaxCherries, getMaxCherries(r + 1, c1 + c11, c2 + c21))
        if c1 == c2: return grid[r][c1] + restMaxCherries
        return grid[r][c1] + grid[r][c2] + restMaxCherries

    return getMaxCherries(0, 0, m - 1)