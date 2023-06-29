from collections import *

inf = (1 << 31) - 1
inp = [
    [inf, -1, 0, inf],
    [inf,inf,inf,-1],
    [inf,-1,inf,-1],
    [0,-1,inf,inf]
]
delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def bfs(i, j, visited):
    queue = deque()
    queue.append(((i, j), 0))

    while(len(queue)):
        (x, y), c = queue.popleft()

        for k in delta:
            dx, dy = x + k[0], y + k[1]
            
            isVisitedCell = visited[dx].get(dy, False)
            if dx < 0 or dx >= len(inp) or dy < 0 or dy >= len(inp[0]) or isVisitedCell: continue
            
            isWallorGate = inp[dx][dy] <= 0
            if isWallorGate: continue

            newCost = min(inp[dx][dy], c + 1)
            inp[dx][dy] = newCost
            queue.append(((dx, dy), newCost))
            visited[dx][dy] = True

def dfs(x, y, c, visited):
    visited[x][y] = True
    for k in delta:
        dx, dy = x + k[0], y + k[1]
        
        isVisitedCell = visited[dx].get(dy, False)
        if dx < 0 or dx >= len(inp) or dy < 0 or dy >= len(inp[0]) or isVisitedCell: continue
        
        isWallorGate = inp[dx][dy] <= 0
        if isWallorGate: continue

        newCost = min(inp[dx][dy], c + 1)
        inp[dx][dy] = newCost
        dfs(dx, dy, newCost, visited)

def findNearestGateForAllRooms():
    for i, r in enumerate(inp):
        for j, c in enumerate(r):
            if c == 0:
                visited = defaultdict(dict)
                visited[i][j] = True
                # bfs(i, j, visited)
                dfs(i, j, 0, visited)

def displayGraph():
    print('-'*50)
    for r in inp: print(r)

displayGraph()
findNearestGateForAllRooms()
displayGraph()