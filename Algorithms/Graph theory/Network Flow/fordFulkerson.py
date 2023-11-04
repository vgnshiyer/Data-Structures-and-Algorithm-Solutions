def search_path(source, sink, parent, visited):
    if source == sink: return True
    
    visited.add(source)
    for ind, val in matrix[source]:
        if ind not in visited and val > 0:
            parent[ind] = source
            if search_path(ind, sink, parent, visited): return True # found path
    return False 
    
def ford_fulkerson(source, sink):
    parent = [-1] * n
    max_flow = 0
    
    while search_path(source, sink, parent, set()):
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