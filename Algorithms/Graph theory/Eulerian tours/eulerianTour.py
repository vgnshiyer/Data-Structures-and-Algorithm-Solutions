'''
Eulerian Cycle: An undirected graph has Eulerian cycle if following two conditions are true. 

* All vertices with non-zero degree are connected. We don’t care about vertices with zero degree because they don’t belong to Eulerian Cycle or Path (we only consider all edges). 
* All vertices have even degree.

Eulerian Path: An undirected graph has Eulerian Path if following two conditions are true. 

* Same as condition (a) for Eulerian Cycle.
* If zero or two vertices have odd degree and all other vertices have even degree. Note that only one vertex with odd degree is not possible in an undirected graph (sum of all degrees is always even in an undirected graph)

In case of a **directed** graph, a graph has eulerian path if

* at most one node has inDegree - outDegree == 1 & at most one node has outDegree - inDegree == 1
* all other nodes have the same in and out degrees

If all nodes have equal inDegrees and outDegrees, we have an eulerian circuit

Time complexity: O(E)
Algorithm:
- We store the in degree count and out degree count for all the nodes
- We take the difference of these numbers
- If the difference is 1 and -1 for exactly two nodes, we know that we have an eulerian path
- We get the start node and do a depth-first-search
- At every node we check the number of outgoing edges (Edges for every node will be stored in the form of a stack)
- we pop every edge and do a dfs.
- Once a node is exhausted, we add it to our path
'''
from collections import defaultdict

graph1 = [[1,2],[2,1],[1,0],[0,1],[2,0],[0,2],[0,3],[3,4],[4,3]]

graph2 = [[1,2],[2,2],[1,3],[3,1],[3,2],[2,4],[2,4],[4,3],[4,6],[6,3],[3,5],[5,6]]

class EulerianTour:
    def setGraph(self, graph):
        self.edges = graph
        self.adj = defaultdict(list)
        self.indegree = defaultdict(int)
        self.outdegree = defaultdict(int)    
        
        ## calculate indegrees and outdegrees
        for u, v in graph:
            self.indegree[v] += 1
            self.outdegree[u] += 1
            self.adj[u].append(v)

    def isValidGraph(self) -> bool:
        sum_ = 0
        for node in self.adj.keys():
            inDeg, outDeg = self.indegree[node], self.outdegree[node]
            sum_ += (inDeg - outDeg)
        return sum_ == 0

    def getStartNode(self) -> int:
        for node in self.adj.keys():
            inDeg, outDeg = self.indegree[node], self.outdegree[node]
            if abs(inDeg - outDeg) == 1: return node
        return list(self.adj.keys())[0]

    def dfs(self, node, path):
        while len(self.adj[node]):
            nextNode = self.adj[node].pop()
            self.dfs(nextNode, path)
        path.append(node)

    def getEulerianPath(self) -> str:
        ## find the eulerian path
        path = []
        self.dfs(self.getStartNode(), path)
        if len(path) >= len(self.edges) + 1: return [] # invalid graph
        return ' '.join(map(str, path[::-1]))

eu = EulerianTour()

eu.setGraph(graph1)
print(eu.getEulerianPath())

eu.setGraph(graph2)
print(eu.getEulerianPath())