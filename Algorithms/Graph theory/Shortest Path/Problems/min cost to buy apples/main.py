from collections import defaultdict
from heapq import *

inf = float('inf')

def djikstra(src, graph) -> dict:
    pq = [(0, src)]
    d = {}
    while pq:
        c, i = heappop(pq)
        if i not in d:
            d[i] = c
            for cj, j in graph[i]:
                heappush(pq, (c + cj, j))
    return d
    

def get_min_cost(n, roads, appleCost, k):
    answer = [inf] * n
    
    graph = defaultdict(list)
    for i, j, c in roads:
        graph[i].append((c, j))
        graph[j].append((c, i))

    for i in range(1, n + 1):
        d = djikstra(i, graph)
        min_cost = inf
        for j in range(1, n + 1):
            apple_cost = d[j] + appleCost[j - 1] + k * d[j]
            min_cost = min(min_cost, apple_cost)
        answer[i - 1] = min_cost
    return answer

if __name__ == '__main__':
    n = 4
    roads = [[1,2,4],[2,3,2],[2,4,5],[3,4,1],[1,3,4]]
    appleCost = [56,42,102,301]
    k = 2
    expected = [54,42,48,51]

    result = get_min_cost(n, roads, appleCost, k)
    print(result)

    assert(result == expected)