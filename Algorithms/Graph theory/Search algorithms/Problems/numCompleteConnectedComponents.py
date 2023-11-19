'''
Every node should be connected to every other node. Therefore number of edges is n * (n - 1 // 2
'''
def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
    adj = defaultdict(list)
    for i, j in edges:
        adj[i].append(j)
        adj[j].append(i)

    visi = set()
    ans = 0

    def dfs(i, nnodes, nedges):
        nnodes[0] += 1
        visi.add(i)

        while adj[i]:
            j = adj[i].pop()
            nedges[0] += 1
            if j not in visi:
                dfs(j, nnodes, nedges)

    for i in range(n):
        if i not in visi:
            nnodes = [0]
            nedges = [0]
            dfs(i, nnodes, nedges)

            if nedges[0] == nnodes[0] * (nnodes[0] - 1):
                ans += 1

    return ans