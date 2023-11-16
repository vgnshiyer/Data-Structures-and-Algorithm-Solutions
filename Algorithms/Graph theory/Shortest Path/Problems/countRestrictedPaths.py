def countRestrictedPaths(n: int, edges: List[List[int]]) -> int:
    d = [-1] * (n + 1)
    dp = [0] * (n + 1)
    adj = defaultdict(list)
    for i, j, k in edges:
        adj[i].append((k, j))
        adj[j].append((k, i))

    heap = [(0, n, -1)]
    while heap:
        c, i, p = heappop(heap)
        if d[i] == -1:
            d[i] = c
            dp[i] = dp[p] if p != -1 else dp[i]
            for c1, j in adj[i]:
                heappush(heap, (c + c1, j, i))
    
    @cache
    def dfs(i):
        if i == n: return 1

        ans = 0
        for _, j in adj[i]:
            if d[i] > d[j]:
                ans += dfs(j)
                ans %= (10 ** 9 + 7)
        return ans

    return dfs(1)
