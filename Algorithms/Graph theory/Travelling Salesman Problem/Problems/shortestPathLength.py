'''
Important thing about TSP is that a node can only be visited once. But this problem allows revisiting node inorder to span the entire graph. 

For using TSP we convert it into a complete graph, by adding direct shortest length paths using the floyyd warshall algorithm. Later we apply TSP.
'''
def shortestPathLength(self, graph: List[List[int]]) -> int:
    n = len(graph)
    dist = [[inf] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
        for j in graph[i]:
            dist[i][j] = 1
            dist[j][i] = 1

    # Floyd Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(
                    dist[i][j],
                    dist[i][k] + dist[k][j]
                )

    dp = {}
    # Traveling salesman
    def TSP(i, mask):
        if mask == (1 << n) - 1:
            return 0 # all nodes explored

        if (i, mask) not in dp:
            ans = inf
            for j in range(n):
                if mask & (1 << j): continue # node already included
                ans = min(ans, dist[i][j] + TSP(j, mask | (1 << j)))
            dp[(i, mask)] = ans
        return dp[(i, mask)]

    shortestPath = inf
    for i in range(n):
        shortestPath = min(shortestPath, TSP(i, (1 << i)))
    return shortestPath
    
'''
We apply a level order traversal while maintaining a state (prev, mask). 
Since we can revisit a node, we take unique pairs of (prev, mask) so that we dont end up on a node from the same path again.

We use level order traversal because this graph is unweighted. All cost will be same (1)
While we could have stored the cost for each node inside the queue itself. But that only adds extra memory as we only need the least number of steps to reach mask == (1 << n) - 1.
'''  
def shortestPathLength_BFS(graph: List[List[int]]) -> int:
    n = len(graph)
    seen = set()
    q = deque()

    for i in range(n):
        q.append((i, 1 << i))
        seen.add((i, 1 << i))

    steps = 0
    while q:
        l = len(q)
        while l:
            i, mask = q.popleft()
            if mask == (1 << n) - 1:
                return steps

            for j in graph[i]:
                if (j, mask | (1 << j)) in seen: continue

                seen.add((j, mask | (1 << j)))
                q.append((j, mask | (1 << j)))
            l -= 1
        steps += 1
