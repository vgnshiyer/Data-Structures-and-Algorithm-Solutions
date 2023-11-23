class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
    
    def find(self, a):
        while a != self.parent[a]:
            self.parent[a] = self.parent[ self.parent[a] ]
            a = self.parent[a]
        return self.parent[a]

    def union(self, a, b):
        self.parent[self.find(a)] = self.parent[self.find(b)]

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, edge in enumerate(edges):
            # append index to the edge for tracking position (after sorting)
            edge.append(i)

        # sort edges by their weights (increasing order)
        edges.sort(key = lambda x : x[2])


        def findMST(**kw):
            without = kw.get('without', None)
            must_include = kw.get('must_include', None)
            dsu = DSU(n)

            mst_cost = 0
            # include edge if must included
            if must_include:
                mst_cost += edges[must_include][2]
                dsu.union(edges[must_include][0], edges[must_include][1])

            for i, (a, b, w, _) in enumerate(edges):
                # exclude if to be excluded
                if i == without: continue
                # if cycle formed
                if dsu.find(a) == dsu.find(b): continue
                # connect the graph
                dsu.union(a, b)
                mst_cost += w

            # avoid edges that disconnect the graph
            for i in range(n):
                if dsu.find(i) != dsu.find(0):
                    return inf

            return mst_cost

        # find min mst cost
        mst_cost = findMST(without = -1)

        critical, psuedo_critical = [], []
        for i in range(len(edges)):
            # exclude current edge
            mst_without_i = findMST(without=i)
            # include current edge
            mst_must_include_i = findMST(must_include=i)
            
            # check whether mst increased
            if mst_without_i > mst_cost:
                # critical edge
                critical.append(edges[i][-1])
            # check whether mst remained same by including the current edge
            elif mst_must_include_i == mst_cost:
                # pseudo critical edge
                psuedo_critical.append(edges[i][-1])

        return [critical, psuedo_critical]