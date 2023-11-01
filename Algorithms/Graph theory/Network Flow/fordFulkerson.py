def search_path(s, t, parent):
    visited = [0] * n
    queue = deque()
    
    queue.append(s)
    visited[s] = True
    
    while queue:
        u = queue.popleft()
        
        for ind, val in enumerate(matrix[u]):
            if not visited[ind] and val > 0: # non zero capacity edge
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
            
    return True if visited[t] else False
    
def ford_fulkerson(source, sink):
    parent = [-1] * n
    max_flow = 0
    
    while search_path(source, sink, parent):
        flow = inf
        s = sink
        
        while s != source:
            flow = min(flow, matrix[ parent[s] ][s])
            s = parent[s]
            
        max_flow += flow
        
        v = sink
        while v != source:
            u = parent[v]
            matrix[u][v] -= flow
            matrix[v][u] += flow
            v = parent[v]
            
    return max_flow      