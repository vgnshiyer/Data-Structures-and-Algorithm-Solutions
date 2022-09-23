### Some Other Important Graph Algorithms worth studying

##### Detecting a cycle in an unidirected graph

given an undirected graph like shown, we need to return whether there is a cycle present in the graph.
        0
       / \
      1   2        cycle here is 2->3->4->2 ... 
         / \
        3---4

Analysis: O(V+E)
- We maintain one visited array tracks whether the node was visited or not.
- We maintain one parent variable which tracks the node where we came from to a node arrived.
- We explore the current unexplored node.
  |-> if neighbour is visited, and is equal to the parent, we skip it.
  |-> if neighbour is unvisited, we call a dfs on that node
  |-> if node is visited, but is not the parent, We have entered a cycle.

##### Detecting a cycle in a directed graph

given an directed graph like below, return whether there is a cycle present in the graph.
                           +---------------+
        0                  |adjacency list:|
       / \                 | 0->1,2        |
      1   2                | 2->3          |
         / \               | 3->4          |
        3---4              | 4->2          | 
                           +---------------+ 
                    cycle here is 2->3->4->2 ... 
Analysis:
- Here we cannot use the previous algorithm to detect cycle in an unidirected graph.
- We maintain two arrays, one for visited, and one for the being_explored(rec stack) nodes.
- If we encounter a node which is not visited, we explore it and mark it as visited in our boolean visited array
- If the node is visited and which is being explored, this means that we have entered a cycle. 

##### Topological Sort

A topological ordering is an ordering of the nodes in a directed graph where for each directed edge from node A to B, node appears before node B in the ordering.
The top sort algorithm can find a topological ordering in O(V+E) time.
NOTE: Topological orderings are not unique. (Multiple valid ways to sort the nodes)

Not every graph can have topological orderging. Specifically graphs with a cycle cannot have a valid ordering. The only graphs that can have a valid topological ordering is a directed acyclic graph(DAG).

By definition, every tree can have a topological ordering, as trees cannot have cycles.
The method to determine the ordering in a tree is to cherry-pick the leaf nodes from the bottom all the way towards the top.

The TOP SORT Algorithm:-
* Pick an unvisited node
* Beginning with the selected node, perform a depth-first-search(DFS) exploring all unvisited nodes only.
* On the recursive call back of the DFS function, add the current node to the topological ordering. 

##### Travelling Salesperson Problem

Given a list of cities, and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once ans returns to the origin city?

In other words: Given a complete graph(every node connected to every other node) with weighted edges, what is the Hamiltonian cycle (path that visits every node exactly once) of the minimum cost?
     A  B  C  D
 A [[0, 4, 1, 9],                A---B
 B  [3, 0, 6, 11],    ->         |\ /|
 C  [4, 1, 0, 2],                |/ \|
 D  [6, 5, -4, 0]]               C---D

Finding the optimal solution for the TSP problem is very hard: in fact, the problem is known to be NP-complete.

The Brute Force approach is to compute the cost for every possible tour. Try all possible permutations. O(n!)
The dynamic programming solution to the TSP problem significantly improves the time complexity to O(n^2 * 2^n). The main idea is to compute the optimal solution for all the subpaths of length N while using the information from the already known optimal partial tours of length N-1.

The Algorithm:
* Select a starting node to designate the start of the tour.
* compute the optimal value for a path from the starting node to every other node. -> this can be obtained by scanning the adjacency matrix. (optimal value for a path with two nodes)
* To compute the optimal value for length of 3, we need to remember two things:
    - the set of visited nodes in the subpath
    - the index of the last visited node in the path
* Together these two things form the state for our DP. There are N possible nodes we could have visited and 2^N subsets of visited nodes. Hence the time complexity of O(N2^N)
* The set of visited nodes is represented as a bit field -> the nodes which are visited will be set in the binary representation of a 32-bit integer.