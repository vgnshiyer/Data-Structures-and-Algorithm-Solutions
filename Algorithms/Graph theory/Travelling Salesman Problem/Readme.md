##### Travelling Salesperson Problem

Given a list of cities, and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once ans returns to the origin city?

In other words: Given a complete graph(every node connected to every other node) with weighted edges, what is the Hamiltonian cycle (path that visits every node exactly once) of the minimum cost?
```
     A  B  C  D
 A [[0, 4, 1, 9],                A---B
 B  [3, 0, 6, 11],    ->         |\ /|
 C  [4, 1, 0, 2],                |/ \|
 D  [6, 5, -4, 0]]               C---D
```

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