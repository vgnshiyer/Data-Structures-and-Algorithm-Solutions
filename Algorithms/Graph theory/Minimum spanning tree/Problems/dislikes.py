'''
This problem introduces a new way to solve bipartite graphs using DSU.

consider this example 

        3---1---2
            |
            4

    We need to form bipartite matching. We color node 1 with RED and nodes (2, 3, 4) with WHITE

However, in disjoint set unions, we used to add nodes which had an edge between them to the same group. We slightly modify the way we assign groups to nodes.

At any node, we check if the current node is connected (belong to same) group as any of the neighbors[1 to len(neighbors) - 1]. If yes, then the graph is not bipartite and cannot be partitioned. 

If not, then we connect all the neighbors of the node together as one component. (Color them all white).
'''
def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
    parent = [i for i in range(n + 1)]

    def find(a):
        while a != parent[a]:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a, b):
        parent[find(b)] = find(a)

    graph = defaultdict(list)
    for a, b in dislikes: 
        graph[a].append(b)
        graph[b].append(a)
    n = len(dislikes)

    for i in range(1, n + 1):
        if not graph[i]: continue
        '''
        we make the neighbors as one component (same color). We make sure that current node does not belong to any of the components
        '''
        b = graph[i][0]
        for a in graph[i][1:]:
            if find(i) == find(a): return False
            union(a, b)

    return True
