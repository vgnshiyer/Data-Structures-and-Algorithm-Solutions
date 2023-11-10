'''
We start a dfs from each node. For every node that is reachable from this node, we add it to its ancestor array and mark it as visited.
'''

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        for i, j in edges:
            adj[i].append(j)

        ancestors = [[] for _ in range(n)]

        def dfs(i, root, visited):
            visited.add(i)
            for j in adj[i]:
                if j not in visited:
                    ancestors[j].append(root)
                    dfs(j, root, visited)

        for i in range(n):
            dfs(i, i, set())

        return ancestors