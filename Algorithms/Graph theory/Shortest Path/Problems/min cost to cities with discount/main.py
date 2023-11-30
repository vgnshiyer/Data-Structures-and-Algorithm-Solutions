from heapq import *
from collections import defaultdict

inf = float('inf')

def min_cost(n, graph, discounts):
    pq = [(0, discounts, 0)]
    d = [[inf] * (discounts + 1) for _ in range(n)]
    while pq:
        c, di, i = heappop(pq)
        if i == n - 1: return c
        if d[i][di] == inf:
            d[i][di] = c
            for cj, j in graph[i]:
                heappush(pq, (c + cj, di, j))
                if di: heappush(pq, (c + cj // 2, di - 1, j))
    return -1

if __name__ == '__main__':
    n = 5
    highways = [[0,1,4],[2,1,3],[1,4,11],[3,2,3],[3,4,2]]
    discounts = 1

    graph = defaultdict(list)
    for i, j, c in highways:
        graph[i].append((c, j))
        graph[j].append((c, i))

    result = min_cost(n, graph, discounts)
    print(result)

    assert result == 9
