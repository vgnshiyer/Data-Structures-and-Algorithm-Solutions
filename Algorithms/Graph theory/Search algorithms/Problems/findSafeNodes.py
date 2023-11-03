def eventualSafeNodes(graph: List[List[int]]) -> List[int]:
    n = len(graph)
    visited = [0] * n
    beingVisited = [0] * n
    safe = [0] * n

    def dfs(node):
        beingVisited[node] = True

        for adj in graph[node]:
            if visited[adj]: continue
            if beingVisited[adj]: return False
            
            if not dfs(adj): 
                safe[node] = 0
                return False

        visited[node] = True
        beingVisited[node] = False
        
        safe[node] = 1
        return True

    for i in range(n):
        if not visited[i]: dfs(i)

    return [i for i in range(n) if safe[i]]