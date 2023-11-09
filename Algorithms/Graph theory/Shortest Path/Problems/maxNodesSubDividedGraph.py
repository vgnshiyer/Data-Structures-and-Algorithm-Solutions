'''
Maximize the amount of maxmoves left at each node when we arrive on it.
Then, for each edge, we can add the minimum of the maxmoves left at each node
'''
def reachableNodes(edges: List[List[int]], maxMoves: int, n: int) -> int:
    adj = defaultdict(dict)
    for u, v, l in edges:
        adj[u][v] = l
        adj[v][u] = l

    heap = [(-maxMoves, 0)]
    d = {}
    while heap:
        moves, i = heappop(heap)
        if i not in d:
            d[i] = -moves # max moves left at i
            for j in adj[i]:
                if j not in d and -moves - adj[i][j] - 1 >= 0:
                    heappush(heap, (moves + adj[i][j] + 1, j))

    ans = len(d)
    for i, j, _ in edges:
        ans += min(d.get(i, 0) + d.get(j, 0), adj[i][j])
    return ans