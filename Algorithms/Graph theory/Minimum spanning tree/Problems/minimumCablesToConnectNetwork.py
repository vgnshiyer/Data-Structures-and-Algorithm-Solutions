'''
We connect the computers until we find an extra cable. We store it.

The number of extra cables we have must at least equal to the (number of disconnected networks) - 1 in our graph.
(For a graph of n components we need atleast n - 1 edges to connect them all)
'''
def makeConnected(n: int, connections: List[List[int]]) -> int:
    if len(connections) < n - 1: return -1

    parent = [i for i in range(n)]
    edge_count = 0

    def find(a):
        while a != parent[a]:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return parent[a]

    def union(a, b):
        parent[find(a)] = parent[find(b)]

    extra_cables = 0
    for c1, c2 in connections:
        if find(c1) != find(c2):
            union(c1, c2)
            edge_count += 1
        else:
            extra_cables += 1
    
    if extra_cables < (n - edge_count) - 1: return -1
    return n - edge_count - 1