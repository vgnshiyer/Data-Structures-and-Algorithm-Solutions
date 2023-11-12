class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.graph = [[inf] * n for _ in range(n)]
        for i in range(n): self.graph[i][i] = 0

        for u, v, w in edges:
            self.graph[u][v] = w

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    self.graph[i][j] = min(
                        self.graph[i][j],
                        self.graph[i][k] + self.graph[k][j]
                    )

    def addEdge(self, edge: List[int]) -> None:
        u, v, w = edge
        if w >= self.graph[u][v]: return
        self.graph[u][v] = w
        n = self.n
        
        for i in range(n):
            for j in range(n):
                self.graph[i][j] = min(
                    self.graph[i][j],
                    self.graph[i][u] + w + self.graph[v][j]
                )

    def shortestPath(self, node1: int, node2: int) -> int:
        w = self.graph[node1][node2]
        return w if w < inf else -1
