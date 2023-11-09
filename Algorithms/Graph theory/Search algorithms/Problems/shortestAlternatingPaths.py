'''
BFS is the best approach for shortest path problems where edges do not have weights. I tried 
'''
def shortestAlternatingPaths(n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
    red = [[0] * n for _ in range(n)]
    blue = [[0] * n for _ in range(n)]

    for i, j in redEdges:
        red[i][j] = 1

    for i, j in blueEdges:
        blue[i][j] = 1

    d = [inf] * n

    q = deque()
    q.append((0, True))
    q.append((0, False))
    visited = set([(0, True), (0, False)])

    l = 0
    while q:
        s = len(q)
        while s:
            i, f = q.popleft()
            d[i] = min(d[i], l)

            for j in range(n):
                if f and red[i][j] and (j, False) not in visited:
                    visited.add((j, False))
                    q.append((j, False))
                if not f and blue[i][j] and (j, True) not in visited:
                    visited.add((j, True))
                    q.append((j, True))
            s -= 1
        l += 1
    return [x if x < inf else -1 for x in d]