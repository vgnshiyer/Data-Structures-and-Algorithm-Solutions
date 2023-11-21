def largestPathValue(colors: str, edges: List[List[int]]) -> int:
    n = len(colors) 
    indegree = [0] * n
    adj = defaultdict(list)
    for i, j in edges:
        adj[i].append(j)
        indegree[j] += 1    # sorting the nodes in topological order
    q = deque()
    for i in range(n):
        if indegree[i] == 0: q.append(i)

    color = [[0] * 26 for _ in range(n)]

    getpos = lambda x : ord(x) - ord('a') 

    res, k = 0, 0
    while q:
        i = q.popleft()
        color[i][getpos(colors[i])] += 1
        res = max(res, color[i][getpos(colors[i])])
        k += 1

        for j in adj[i]:
            indegree[j] -= 1
            # pushing the best value found so far for each color forward into the paths
            for x in range(26):
                color[j][x] = max(color[j][x], color[i][x])
            if indegree[j] == 0:
                q.append(j)

    return -1 if k != n else res