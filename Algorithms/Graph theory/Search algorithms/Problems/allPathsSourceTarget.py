def allPathsSourceTarget(graph: List[List[int]]) -> List[List[int]]:
    paths = []
    n = len(graph)
    
    def dfs(node, parent):
        if node == n - 1:
            path = []
            while node != parent[node]:
                path = [node] + path
                node = parent[node]
            paths.append([node] + path)
            return

        for adj in graph[node]:
            parent[adj] = node
            dfs(adj, parent)

    dfs(0, [x for x in range(n)])
    return paths