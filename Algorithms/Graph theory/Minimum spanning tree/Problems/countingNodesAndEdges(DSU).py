class DSU:
    def __init  __(self, n):
        self.n = n
        self.parent = [i for i in range(n)]
        # initialize each node to be a component by its own
        self.size = [1] * n
        self.edge_count = [0] * n

    def find(self, a):
        if a != self.parent[a]:
            # collapse all the parents so that all belong to a single group
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        # count an edge to the main joining component
        self.edge_count[pa] += 1
        if pa != pb:
            # merge component b to a
            self.parent[pb] = pa
            # include all nodes in b to size(a)
            self.size[pa] += self.size[pb]
            # include all edges counted in b so far to a
            self.edge_count[pa] += self.edge_count[pb]

def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
    dsu = DSU(n)

    # create components
    for i, j in edges: dsu.union(i, j)

    ans = 0
    for i in range(n):
        # finding parent of component
        if i == dsu.parent[i]:
            # checking if graph is complete
            if (dsu.size[i] * (dsu.size[i] - 1) // 2) == dsu.edge_count[i]: ans += 1

    return ans