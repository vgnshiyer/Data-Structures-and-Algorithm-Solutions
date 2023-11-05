'''
With exactly one extra node, we can have three cases

(1) Node with 2 parents

      x   x
       \ /
        v
        x
  Remove any one edge      

(2) Graph has cycle

      x-->x
      ^   |
      |   v
      x<--x
  Remove latest cycle forming edge
  
(3) Graph has cycle and 2 parent node

      x-->x<--x
      ^   |
      |   v
      x<--x    
  Remove one extra edge.
  Check if the graph is valid ==> Remove that edge
  If cycle formed, wrong edge was removed. ==> Remove first extra edge
  If no cycle formed, check number of components. (Graph may be split into two) ==> remove first edge
  Remove second edge if all above checks were successful.    
'''
def findRedundantDirectedConnection(edges: List[List[int]]) -> List[int]:
    n = len(edges)
    parent = [i for i in range(n + 1)]

    def find(a):
        while a != parent[a]:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return parent[a]

    def union(a, b):
        parent[find(b)] = find(a)

    second, first = None, None
    p = {}
    for u, v in edges:
        if v in p: # found second parent to a node
            first = [p[v], v]
            second = [u, v]
            break
        p[v] = u

    edge_count = 0
    for u, v in edges:
        if [u, v] == second: continue # do not add second extra edge
        if find(u) != find(v):
            union(u, v)
            edge_count += 1
        else: # found a cycle forming edge
            if not second:
                return [u, v]
            else: return first

    if n - edge_count == 1: # one component formed
        return second

    return first