def removeStones(self, stones: List[List[int]]) -> int:
    n = len(stones)
    edges = []

    for i in range(n):
        for j in range(i + 1, n):
            if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                edges.append((i, j))

    parent = [i for i in range(n)]

    def find(a):
        while a != parent[a]:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a, b):
        parent[find(b)] = parent[find(a)]

    cnt = 0
    for a, b in edges:
        if find(a) != find(b):
            cnt += 1 ## this counts the number of edges in the mst. 
            '''Remember, in an MST, a connected component of size n has exactly n - 1 edges.'''
            union(a, b)
    
    return cnt

def removeStones(stones: List[List[int]]) -> int:
    n = len(stones)
    graph = defaultdict(list)

    for i in range(n):
        for j in range(i, n):
            if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                graph[i].append(j)
                graph[j].append(i)

    visited = [0] * n

    def dfs(i):
        visited[i] = 1
        for j in graph[i]:
            if not visited[j]: dfs(j)

    cnt = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            cnt += 1

    '''
    In this problem we can remove at most n - 1 stones from a connected component of size n.
    Consider components n1 and n2
    n1 + n2 = n

    ans = (n1 - 1) + (n2 - 1)
        = n - 2
        = n - (number of connected components)
    '''
    return n - cnt