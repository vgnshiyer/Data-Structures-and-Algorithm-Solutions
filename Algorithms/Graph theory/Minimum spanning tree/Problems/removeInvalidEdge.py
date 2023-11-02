
def findRedundantConnection(edges: List[List[int]]) -> List[int]:
    n = len(edges)
    parent = {}
    for i in range(1, n + 1): parent[i] = i

    def find(a):
        while a != parent[a]:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a, b):
        pa, pb = find(a), find(b)
        parent[pb] = pa

    for a, b in edges:
        if find(a) == find(b): return a, b
        else: union(a, b)