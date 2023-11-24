class DSU:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n + 1))

    def find(self, a):
        if a != self.parent[a]:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        self.parent[self.find(b)] = self.parent[self.find(a)]

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # collect all type 3 edges (both can travel)
        type_3 = [(x, y) for i, x, y in edges if i == 3]

        # collect all type 1 edges (only alice can travel)
        type_1 = [(x, y) for i, x, y in edges if i == 1]

        # collect all type 2 edges (only bob can travel)
        type_2 = [(x, y) for i, x, y in edges if i == 2]

        dsu = DSU(n)

        removals = 0
        alice = 0
        bob = 0

        # using all common edges
        for a, b in type_3:
            if dsu.find(a) != dsu.find(b):
                dsu.union(a, b)
                # count edges for both alice and bob
                alice += 1
                bob += 1
            else:
                # remove type 3 edge
                removals += 1
        # storing parent copy for bob's graph computation
        parent_copy = dsu.parent.copy()

        # using all alice's edges
        for a, b in type_1:
            if dsu.find(a) != dsu.find(b):
                dsu.union(a, b)
                # count for alice
                alice += 1
            else:
                # remove type 1 edge
                removals += 1

        dsu.parent = parent_copy
        # using all bob's edges
        for a, b in type_2:
            if dsu.find(a) != dsu.find(b):
                dsu.union(a, b)
                # count for bob
                bob += 1
            else:
                # remove type 2 edge
                removals += 1

        # return removals if graph is fully connected
        return removals if alice == bob == n - 1 else -1