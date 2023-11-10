'''
Apply floyyd warshall. Find APSP. Get min reachable nodes less than threshold.
'''

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [[inf] * n for _ in range(n)]
        for i in range(n): graph[i][i] = 0

        for i, j, w in edges:
            graph[i][j] = w
            graph[j][i] = w

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    graph[i][j] = min(
                        graph[i][j],
                        graph[i][k] + graph[j][k]
                    )

        for i in range(n):
            for j in range(n):
                graph[i][j] = 1 if graph[i][j] <= distanceThreshold else 0

        m = inf
        city = -1
        for i in range(n):
            reaching = sum(graph[i])
            if reaching <= m: 
                m = reaching
                city = i
        return city