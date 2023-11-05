def shortestPathLength(self, graph: List[List[int]]) -> int:
    n = len(graph)
    dist = [[inf] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
        for j in graph[i]:
            dist[i][j] = 1
            dist[j][i] = 1

    # Floyd Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(
                    dist[i][j],
                    dist[i][k] + dist[k][j]
                )

    dp = {}
    # Traveling salesman
    def TSP(i, mask):
        if mask == (1 << n) - 1:
            return 0 # all nodes explored

        if (i, mask) not in dp:
            ans = inf
            for j in range(n):
                if mask & (1 << j): continue # node already included
                ans = min(ans, dist[i][j] + TSP(j, mask | (1 << j)))
            dp[(i, mask)] = ans
        return dp[(i, mask)]

    shortestPath = inf
    for i in range(n):
        shortestPath = min(shortestPath, TSP(i, (1 << i)))
    return shortestPath