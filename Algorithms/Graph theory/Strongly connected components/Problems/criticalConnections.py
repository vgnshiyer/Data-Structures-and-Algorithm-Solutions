def criticalConnections(n: int, connections: List[List[int]]) -> List[List[int]]:
    time = 0
    tin = [-1] * n
    low = [-1] * n
    bridges = []

    adj = defaultdict(list)
    for i, j in connections:
        adj[i].append(j)
        adj[j].append(i)

    def dfs(i, p = -1):
        nonlocal time
        tin[i] = time
        low[i] = time
        time += 1

        for j in adj[i]:
            if j == p: continue
            if tin[j] == -1:
                dfs(j, i)
                low[i] = min(low[i], low[j])
                if low[j] > tin[i]: bridges.append((i, j))
            else:
                low[i] = min(low[i], low[j])

    for i in range(n):
        if tin[i] == -1: dfs(i)
    return bridges