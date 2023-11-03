def isBipartite(graph: List[List[int]]) -> bool:
    n = len(graph)
    color = [-1] * n
    
    def isBipartite(i, p=-1):
        for j in graph[i]:
            if j == p: continue
            if color[j] == color[i]: return False
            if color[j] != -1: continue

            color[j] = color[i] ^ 1
            if not isBipartite(j, i): return False
        return True
    
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            if not isBipartite(i): return False
    return True
    
def isBipartite_bfs(adj, n):
    '''
    Create a graph color which represents the group that a node belongs to
    - -1 -> no group
    - 0 -> group 0
    - 1 -> group 1
    '''
    color = [-1] * n
    
    queue = deque()
    queue.append(0)
    
    while queue:
        u = queue.popleft()
        
        for v in range(n):
            if u != v:
                if adj[u][v] and color[v] == -1:
                    color[v] = 1 - color[u] # give a different color to v
                elif color[v] == color[u]: return False # graphs of different sets must have different color
                
    return True  