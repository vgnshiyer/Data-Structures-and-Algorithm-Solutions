def closestMeetingNode(edges: List[int], node1: int, node2: int) -> int:
    '''
    Essentially the problem is asking to find the node which is between node1 and node2 such that the distance to travel from either of them is the minimum. We need to find the minimum maximum of the shortest distance from node1 and node2 to all the other nodes.
    '''
    n = len(edges)
    adj = defaultdict(list)
    for i, j in enumerate(edges):
        if j != -1:
            adj[i].append(j)

    def bfs(n, d):
        d[n] = 0
        q = deque([n])
        while q:
            l = len(q)
            for _ in range(l):
                i = q.popleft()
                for j in adj[i]:
                    if d[j] > d[i] + 1:
                        d[j] = 1 + d[i]
                        q.append(j)
    d1 = [inf] * n
    d2 = [inf] * n
    
    bfs(node1, d1)
    bfs(node2, d2)

    min_dist = inf
    min_id = -1
    for i in range(n):
        if d1[i] != inf and d2[i] != inf:
            if min_dist > max(d1[i], d2[i]):
                min_dist = max(d1[i], d2[i])
                min_id = i
    return min_id