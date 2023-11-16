'''
visited can be passed without creating a copy 
with visited | set([new_node])
'''
def maximalPathQuality(values: List[int], edges: List[List[int]], maxTime: int) -> int:
    self.maxQuality = 0
    adj = defaultdict(list)
    for i, j, k in edges:
        adj[i].append((j, k))
        adj[j].append((i, k))
    
    def dfs(node, visited, cost, gain):
        if node == 0:
            self.maxQuality = max(self.maxQuality, gain)
        for nei, c in adj[node]:
            if cost >= c:
                dfs(nei, visited | set([nei]), cost - c, gain + (values[nei] if nei not in visited else 0))

    dfs(0, set([0]), maxTime, values[0])
    return self.maxQuality