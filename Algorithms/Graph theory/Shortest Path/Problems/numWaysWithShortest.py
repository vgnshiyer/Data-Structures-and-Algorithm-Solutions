'''
Djikstra + DP
 - find number of ways to reach target with the shortest path.
 - if we find a path to a node with the same distance as found before, we add the number of ways we had reached to its parent to it.
'''
def countPaths(n: int, roads: List[List[int]]) -> int:
    graph = defaultdict(list)
    for i, j, t in roads:
        graph[i].append((t, j))
        graph[j].append((t, i))

    mod = 10 ** 9 + 7

    d = [-1] * n
    dp = [0] * n
    dp[0] = 1 # 1 way to reach the src node
    heap = [(0, 0, -1)]
    while heap:
        t, i, p = heappop(heap)
        if d[i] == -1:
            d[i] = t
            dp[i] = dp[p] if p != -1 else dp[i]
            for t1, j in graph[i]:
                heappush(heap, (t + t1, j, i))
        elif d[i] == t:
            dp[i] += dp[p]
            dp[i] %= mod

    return dp[n - 1]