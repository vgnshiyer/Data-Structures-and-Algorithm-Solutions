'''
Sort queries based on weight and sort edges based on weight as well. Scan through queries from lowest to highest weight and connect the edges whose weight strictly fall below this limit. Check if the queried nodes p and q are connected in Union-Find structure. If so, put True in the relevant position; otherwise put False.
'''
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
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        for i in range(len(queries)):
            queries[i].append(i) ## using this to preserve the index of queries after sorting

        comp = lambda x : x[2]

        # sort queries by weights
        queries.sort(key = comp)
        # sort edgelist by weights
        edgeList.sort(key = comp)

        dsu = DSU(n)

        i = 0
        ans = [False] * len(queries)
        for q in queries:
            w = q[2]

            # connect only edges whose weights are less than w
            while i < len(edgeList) and edgeList[i][2] < w:
                a, b = edgeList[i][:2]
                if dsu.find(a) != dsu.find(b):
                    dsu.union(a, b)
                i += 1
            
            # verify if qj was reachable with edges with weights less than w
            ans[q[3]] = dsu.find(q[0]) == dsu.find(q[1])

        return ans