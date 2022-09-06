### Graph Algorithms

##### Shortest Path
In graph theory, the problem of finding a path between two nodes in a graph, such that the sum of weights of the edges of the path is minimum, is known as the Shortest Path.

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