def possibleBipartition_bfs(n: int, dislikes: List[List[int]]) -> bool:
    color = [-1] * (n + 1)
    graph = defaultdict(list)
    for a, b in dislikes: 
        graph[a].append(b)
        graph[b].append(a)
    
    q = deque()
    for i in range(1, n + 1):
        if color[i] != -1: continue

        color[i] = 0
        q.append(i)
        while q:
            i = q.popleft()
            for j in graph[i]:
                if color[j] != -1 and color[j] == color[i]: return False
                if color[j] == -1:
                    color[j] = 1 ^ color[i]
                    q.append(j)

    return True

def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
    color = [-1] * (n + 1)
    graph = defaultdict(list)
    for a, b in dislikes: 
        graph[a].append(b)
        graph[b].append(a)
        
    def dfs(i):
        for j in graph[i]:
            if color[j] != -1 and color[i] == color[j]: return False
            if color[j] == -1:
                color[j] = 1 - color[i]
                if not dfs(j): return False
        return True

    for i in range(1, n + 1):
        if color[i] == -1:
            color[i] = 0
            if not dfs(i): return False
    return True

