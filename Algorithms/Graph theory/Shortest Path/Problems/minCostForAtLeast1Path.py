'''
Djikstra will only explore a path if it is better than a previous path.
Key point: Whenever we want to find a shortest path from a node to every other node, we do a bfs/djikstra from dest.
'''
def minCost(grid: List[List[int]]) -> int:
    d = {}
    n, m = len(grid), len(grid[0])
    heap = [(0, n - 1, m - 1)]
    while heap:
        c, i, j = heappop(heap)
        if (i, j) not in d:
            d[(i, j)] = c

            # up
            if i - 1 >= 0 and grid[i - 1][j] == 3:
                heappush(heap, (c, i - 1, j))
            elif i - 1 >= 0: heappush(heap, (c + 1, i - 1, j))

            # down
            if i + 1 < n and grid[i + 1][j] == 4:
                heappush(heap, (c, i + 1, j))
            elif i + 1 < n: heappush(heap, (c + 1, i + 1, j))

            # left
            if j - 1 >= 0 and grid[i][j - 1] == 1:
                heappush(heap, (c, i, j - 1))
            elif j - 1 >= 0: heappush(heap, (c + 1, i, j - 1))

            # right
            if j + 1 < m and grid[i][j + 1] == 2:
                heappush(heap, (c, i, j + 1))
            elif j + 1 < m: heappush(heap, (c + 1, i, j + 1))

    return d[(0, 0)]

