### Graph Algorithms

### Shortest Path
In graph theory, the problem of finding a path between two nodes in a graph, such that the sum of weights of the edges of the path is minimum, is known as the Shortest Path.

**Problem Cues**
If the problem wants an optimal path or the cost of a minimal route or journey, it is likely a shortest path problem. Even if a graph isn't obvious in a problem, if the problem wants the minimum cost of some process and there aren't many states, then it is usually easy to superimpose a graph on it. The big point here: shortest path = search for the minimal cost way of doing something.

If the graph is unweighted, the shortest path contains a minimal number of edges. A breadth first search (BFS) will solve the problem in this case, using a queue to visit nodes in order of their distance from the source. If there are many vertices but few edges, this runs much faster than Dijkstra's algorithm.

If negative weight edges are allowed, Dijkstra's algorithm breaks down. Fortunately, the Floyd-Warshall algorithm isn't affected so long as there are no negative cycles in the graph (if there is a negative cycle, it can be traversed arbitrarily many times to get ever `shorter' paths). So, graphs must be checked for them before executing a shortest path algorithm.

It is possible to add additional conditions to the definition of shortest path (for example, in the event of a tie, the path with fewer edges is shorter). So long as the distance function can be augmented along with the comparison function, the problem remains the same. In the example above, the distance function contains two values: weight and edge count. Both values would be compared if necessary.

##### Below are some of the most commonly used algorithms.
Each Algorithm has its own advantages and disadvantages. Depending on the use case, it is expected by a good problem solver to select the most appropriate and efficient algorithm.

* **BFS**
The breadth first search Algorithm is the best choice to find the shortest path in a graph with no weights attached to the edges. It gives a time complexity of O(E+V) -> (E for the algorithm to explore all the edges and V for initializing the visited array) 
ps: (DFS also has same time complexity)

* **Dijkstra's Algorithm**
The above BFS approach, although faster may fail in case of a weighted graph with directed edges. That is where, Dijkstra's Algo comes into picture.
Dijkstra's Algorithm is an algorithm of finding the shortest path between any two nodes in a weighted directed graph. It follows a greedy approach of always selecting the nearest available node and exploring it. If it finds a path to an unexplored node which is shorter than the already existing path, it relaxes that path and continues.
Time Complexity: O((E+V)*LogV) -> using a priority queue(min heap) (* V for APSP)

* **Floyd Warshall**
Although Dijkstra's Algorithm works well for a problem to find the shortest path between any two nodes in a weighted directed graph, it fails when there are negative edges in a graph. 
The Floyd Warhsall Algorithm solves this problem of negative edges by using the concept of Dynamic Programming, at the expense of some extra computation(increased time complexity). However, it is wise to only use this algorithm when the graph is known to have negative edges and we need to find all pair shortest path. It is foolish to use this algorithm for a problem which asks shortest path between just two nodes, in a graph with no negative edges.
Time Complexity: O(V^3)

* **Bellman Ford**
The Bellman Ford Algorithm is a Single Source Shortest Path Algorithm. However, it is not ideal for most single source problems as it has a time complexity of O(EV). It is better to use Dijkstra's Algorithm which has a TC of O((E+V)*LogV) using a min heap. In order to solve the limitation of Dijkstra's algorithm of failing to perform when the graph has negative edges, the Bellman Ford Algorithm can be used to find shortest path on a graph with negative edges, and also detect negative cycles in the graph.
Time Complexity: O(EV)

![Alt text](graph.jpeg?raw=true "Graph Algorithms Side-By-Side")

### Minimum Spanning Trees
**An analogy:** Farmer John is bringing internet connectivity to all farms in the area. He has ordered a high speed connection for his farm and is going to share his connectivity with the other farmers. To minimize cost, he wants to minimize the length of optical fiber to connect his farm to all the other farms.

Given a list of how much fiber it takes to connect each pair of farms, find the minimum amount of fiber needed to connect them all together. Each farm must connect to some other farm such that a path exists from any farm to any other farm. Some farms might have 1, 2, 3, or more connections to them.

**The Abstraction:**
Given: an undirected, connected graph with weighted edges

A spanning tree of a graph is any sub-graph which is a connected tree (i.e., there exists a path between any nodes of the original graph which lies entirely in the sub-graph).

A minimal spanning tree is a spanning tree which has minimal `cost' (where cost is the sum of the weights of the edges in the tree).

**Problem Cues:**
If the problem mentions wanting an optimal, connected sub-graph, a minimum cost way to connect a system together, or a path between any two parts of the system, it is very likely to be a minimum spanning tree problem.

If you subject the tree to any other constraints (no two nodes may be very far away or the average distance must be low), this algorithm breaks down and altering the program to handle such constraints is very difficult.

There is obviously no problem with multiple edges between two nodes (you ignore all but the smallest weight).

Prim's algorithm does not extend to directed graphs (where you want strong connectedness), either.

TO - BE - WRITTEN (prims and kruskals)
##### Below are some of the most commonly used algorithms.

* **Prim's Algorithm**
A greedy algorithm which always starts from one of the nodes in the graph, moves through several adjacent nodes, in order to explore the entire graph. At every point, the algorithm always selects the edge with minimum weight that is connected to the nodes currently in the tree.

* **Kruskal's Algorithm**
Another Greedy algorithm which works on the same principle of selecting the least cost edges available. But there is a difference here. It selects the edges available in such a way that the resulting MST does not form a cycle in it. If it does, then the edge will be discarded.

In order to implement Kruskal's Algorithm, we use the concept of Disjoint Set Union. Here, the nodes belonging to the edges that are added to the MST are considered to be part of a Disjoint Set. Once an edge is added, we check whether the nodes belong to the same subset or not, using the Find operation. If not, we simple unite the two subsets using the Union Operation. If they do, the edge forms a cycle. 

### The Dichotomies between MSTs and Shortest path Algos

***Shortest Paths*** Here, you are only concerned about the path to travel between two nodes. You optimize this path in such a way that the total cost to travel from it is minimized. 

***MSTs*** Here, you start from one point, with the goal of reaching(spanning) all the nodes present in the graph. Therefore, you may not end up always chosing the shortest path between any two nodes. Instead, you focus on chosing the path which will lead to a shorter path for all the nodes in your graph.

**An analogy to understand better:** You are a food delivery company. Your goal is to deliver food to multiple locations by covering the distance in the most optimal way with minimum possible time spent. => You will use Minimum Spanning Trees.

If you want to deliver food only to one location intead, => You will use Shortest Paths.

**An Example** 
![Alt text](b6Ggp.png?raw=true "example")

The spanning tree looks like below. This is because if we add up the edges in this configuration, we get the least total cost possible: 2+5+14+4=25.

(1)   (4)
  \   /
   (2)           (Important detail to notice -> no. of edges in an MST = no. of vertices -1)
  /   \          (no. of MSTs possible = eC(n-1) - no. of cycles)
(3)   (5)

Notice that the minimum cost according to the spanning tree to reach node (4) from node (1) is 7(2+5). However, according to shortest path algorithms, we would find that there is a direct shorter path from node (1)  to (4).

### Eulerian Tour

A path which uses every edge exactly once is called an Eulerian path. If the path begins and ends on the same vertex, it is called a Eulerian circuit.

If your graph does not have an Eulerian circuit, you may not be able to return to your starting node or not be able to traverse all the edges in the graph.

If a graph contains Eulerian circuit, it also a contains Eulerian path.

**The Algorithm**
Detecting whether a graph has an Eulerian tour or circuit is actually easy; two different rules apply.

* A graph has an Eulerian circuit if and only if it is connected (once you throw out all nodes of degree 0) and every node has `even degree'.
* A graph has an Eulerian path if and only if it is connected and every node except two has even degree.
* In the second case, one of the two nodes which has odd degree must be the start node, while the other is the end node.

The basic idea of the algorithm is to start at some node the of graph and determine a circuit back to that same node. Now, as the circuit is added (in reverse order, as it turns out), the algorithm ensures that all the edges of all the nodes along that path have been used. If there is some node along that path which has an edge that has not been used, then the algorithm finds a circuit starting at that node which uses that edge and splices this new circuit into the current one. This continues until all the edges of every node in the original circuit have been used, which, since the graph is connected, implies that all the edges have been used, so the resulting circuit is Eulerian.

More formally, to determine a Eulerian circuit of a graph which has one, pick a starting node and recurse on it. At each recursive step:

* Pick a starting node and recurse on that node. At each step:
* If the node has no neighbors, then append the node to the circuit and return
* If the node has a neighbor, then make a list of the neighbors and process them (which includes deleting them from the list of nodes on which to work) until the node has no more neighbors
* To process a node, delete the edge between the current node and its neighbor, recurse on the neighbor, and postpend the current node to the circuit.

**Example Problem**

Given a collection of cities, along with the flights between those cities, determine if there is a sequence of flights such that you take every flight exactly once, and end up at the place you started.

Analysis: This is equivalent to finding a Eulerian circuit in a directed graph.

