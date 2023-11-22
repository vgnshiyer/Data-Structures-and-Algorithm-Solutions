def minimumFuelCost(roads: List[List[int]], seats: int) -> int:
    adj = defaultdict(list)
    for a, b in roads:
        adj[a].append(b)
        adj[b].append(a)
    self.ans = 0

    def dfs(i, prev, p=1):
        for j in adj[i]:
            if j != prev:
                p += dfs(j, i)
        self.ans += ceil(p / seats) if i else 0
        return p

    dfs(0, 0)
    return self.ans
