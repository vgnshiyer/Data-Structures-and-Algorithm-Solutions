def isBipartite(adj, n):
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