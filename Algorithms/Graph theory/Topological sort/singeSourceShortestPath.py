def SSSP(src):

    order = []
    for i in range(n):
        if not visited[i]: topSort(i) # sorting the graph topologically

    dist = [inf] * n
    dist[src] = 0

    for node in order: # when we get to a node, all nodes before it in the order will have been processed -> guarantees that we have the best cost for this node.
        for child, cost in adj[node]:
            dist[child] = min(dist[child], dist[node] + cost) # relaxation step
    
    return dist # min dist from src to all other node