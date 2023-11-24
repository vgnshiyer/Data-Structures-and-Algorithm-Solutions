class DSU:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def find(self, a):
        if a != self.parent[a]:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if self.find(a) != self.find(b):
            self.parent[pa] = self.parent[pb]
            self.size[pb] += self.size[pa]

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)

        for i, j in edges:
            dsu.union(i, j)

        ans = 0
        for i in range(n):
            ans += (n - dsu.size[dsu.find(i)])
        return ans // 2
