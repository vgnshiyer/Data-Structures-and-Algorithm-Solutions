## DFS solution: Visit all possible nodes from 0. Prune if a restricted node occurs
def reachableNodes(n: int, edges: List[List[int]], restricted: List[int]) -> int:
    restricted = set(restricted)
    adj = defaultdict(list)
    for i, j in edges: 
        adj[i].append(j)
        adj[j].append(i)

    self.ans = 0

    def dfs(i):
        self.ans += 1
        restricted.add(i)
        for j in adj[i]:
            if j not in restricted:
                dfs(j)

    dfs(0)
    return self.ans
    
## BFS solution: Level order traversal. Prune when a restricted node occurs
def reachableNodes(n: int, edges: List[List[int]], restricted: List[int]) -> int:
    restricted = set(restricted)
    adj = defaultdict(list)
    for i, j in edges: 
        adj[i].append(j)
        adj[j].append(i)

    res = 0
    restricted.add(0)

    q = deque([0])
    while q:
        i = q.popleft()
        res += 1
        for j in adj[i]:
            if j not in restricted:
                q.append(j)
                restricted.add(j)

    return res

## DSU solution: Connect all possible components and track their sizes. Return the size of the zeroth component.
class DSU:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, a):
        while a != self.parent[a]:
            self.parent[a] = self.parent[ self.parent[a] ]
            a = self.parent[a]
        return self.parent[a]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa != pb:
            self.parent[pb] = pa
            self.size[pa] += self.size[pb]

    def get_size(self, a):
        return self.size[ self.find(a) ]

def reachableNodes(n: int, edges: List[List[int]], restricted: List[int]) -> int:
    restricted = set(restricted)
    dsu = DSU(n)
    
    for i, j in edges:
        if i in restricted or j in restricted: continue
        dsu.union(i, j)

    return dsu.get_size(0)  