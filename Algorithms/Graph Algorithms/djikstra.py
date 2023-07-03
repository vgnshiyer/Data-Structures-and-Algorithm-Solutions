'''
* check if curr node is in the distance hashset or not
* if not, create an entry and add the current cost
* if present, find minimum and add
* in this approach, we push the new cost in the heap regardless of it being best or worst value
* notice that we do not need the visited boolean array in this approach
'''

def djikstra(edges, N, K):
    q, d, adj = [(0, K)], {}, collections.defaultdict(list)
    for u, v, w in edges:
        adj[u].append((v, w))
    while q:
        cost, node = heapq.heappop(q)
        if node not in d: 
            d[node] = cost
            for v, w in adj[node]:
                heapq.heappush(q, (cost + w, v))
        else:
            d[node] = min(d[node], cost)
    return d

## normal implementation (more intuitive)
def djikstra(edges, N, K):
    q, d, adj, visited = [(0, K)], [10**8 for i in range(N+1)], collections.defaultdict(list), set()
    for u, v, w in edges:
        adj[u].append((v, w))
    d[K] = 0
    while q:
        cost, node = heapq.heappop(q)
        visited.add(node)

        for v, w in adj[node]:
            if v in visited: continue
            if w + cost < d[v]:
                d[v] = w + cost
                heapq.heappush(q, (d[v], v))
    return d
