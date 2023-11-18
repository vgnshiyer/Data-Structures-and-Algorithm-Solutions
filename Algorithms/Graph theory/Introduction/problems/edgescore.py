def edgeScore(edges: List[int]) -> int:
    n = len(edges)
    edgescore = [0] * n
    for i in range(n):
        to = edges[i]
        edgescore[to] += i
    return sorted(range(n), key = lambda x : (-edgescore[x], x))[0]