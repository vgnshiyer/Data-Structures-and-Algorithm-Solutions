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
    
def largestPathValue(colors: str, edges: List[List[int]]) -> int:
    n = len(colors)
    visited = [0] * n
    color = [[0] * 26 for _ in range(n)]
    adj = defaultdict(list)
    for i, j in edges: adj[i].append(j)

    # function to calculate position for character
    getpos = lambda x : ord(x) - ord('a')
    
    def dfs(i):
        if not visited[i]:
            # visited for the first time
            visited[i] = 1
            for j in adj[i]:
                if dfs(j) == inf: return inf
                # tracking the best value for each color after exploring a single path
                for k in range(26):
                    # using a pull dp approach
                    color[i][k] = max(color[i][k], color[j][k])
            # track current color
            color[i][getpos(colors[i])] += 1

            # at this point the node is fully visited without cycles
            visited[i] = 2

        # if node was not visited fully (being visited), return inf
        return inf if visited[i] != 2 else color[i][getpos(colors[i])]

    res = 0
    for i in range(n):
        # find max frequence of a color at every node
        res = max(res, dfs(i))
    return res if res != inf else -1
