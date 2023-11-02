def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    d = {}
    adj = defaultdict(list)
    for u, v, t in times: adj[u].append((v, t))
    heap = [(0, k)]

    while heap:
        cost, cur = heapq.heappop(heap)
        if cur not in d:
            d[cur] = cost
            for nxt in adj[cur]:
                heapq.heappush(heap, (cost + nxt[1], nxt[0]))

    return max(d.values()) if len(d.values()) == n else -1