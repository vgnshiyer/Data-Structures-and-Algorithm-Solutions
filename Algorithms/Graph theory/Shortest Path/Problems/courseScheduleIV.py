'''
If a is prereq of b, and b is prereq of c, then a is prereq of c.
a -> b -> c

n^3 approach:
- use floyyd warshall algo and form direct paths between nodes.
'''
def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
    graph = [[0] * n for _ in range(n)]

    for i, j in prerequisites:
        graph[i][j] = 1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = graph[i][j] | (
                    graph[i][k] & graph[k][j]
                )

    return [
        graph[i][j] for i, j in queries
    ]