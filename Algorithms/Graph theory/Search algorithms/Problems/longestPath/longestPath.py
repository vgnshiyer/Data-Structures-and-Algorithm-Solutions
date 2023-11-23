def longestPath(self, p: List[int], s: str) -> int:
    self.best = 1
    adj = defaultdict(list)
    n = len(s)
    for i in range(n):
        if p[i] == -1: continue
        adj[i].append(p[i])
        adj[p[i]].append(i)

    def dfs(i, p = -1):
        max1, max2 = 0, 0
        for j in adj[i]:
            if j == p: continue
            branch = dfs(j, i)

            if s[j] == s[i]: continue
            if branch > max1: 
                max2 = max1
                max1 = branch
            elif branch > max2: max2 = branch
        
        with_splitting = max1 + max2 + 1
        without_splitting = max1 + 1

        self.best = max(self.best, max(with_splitting, without_splitting))
        return without_splitting

    dfs(0)
    return self.best