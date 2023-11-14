def networkBecomesIdle(edges: List[List[int]], p: List[int]) -> int:
    d = {}
    n = len(p)
    adj = defaultdict(list)
    for i, j in edges:
        adj[i].append(j)
        adj[j].append(i)

    q = deque([0])
    visited = set([0])
    seconds = 0
    while q:
        l = len(q)
        while l:
            i = q.popleft()
            d[i] = seconds
            for j in adj[i]:
                if j not in visited:
                    visited.add(j)
                    q.append(j)
            l -= 1
        seconds += 1

    max_time = -1
    for i in range(1, n):
        time_to_master = d[i] * 2
        total_time = ((time_to_master - 1) // p[i]) * p[i] + time_to_master + 1
        max_time = max(max_time, total_time)

    return max_time