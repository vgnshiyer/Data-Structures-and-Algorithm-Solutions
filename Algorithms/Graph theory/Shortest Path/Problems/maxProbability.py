'''
Simple djikstra implementation
'''
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            adj[u].append((v, succProb[i]))
            adj[v].append((u, succProb[i]))

        heap = [(-1, start_node)]
        d = {}
        while heap:
            p, i = heappop(heap)
            if i not in d:
                d[i] = -p
                for j, pj in adj[i]:
                    heappush(heap, (p * pj, j))

        return d.get(end_node, 0)
