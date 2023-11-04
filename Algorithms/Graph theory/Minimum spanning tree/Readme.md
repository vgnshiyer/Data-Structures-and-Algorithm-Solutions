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

##### Below are some of the most commonly used algorithms.

* **Prim's Algorithm**
A greedy algorithm which always starts from one of the nodes in the graph, moves through several adjacent nodes, in order to explore the entire graph. At every point, the algorithm always selects the edge with minimum weight that is connected to the nodes currently in the tree.

* **Kruskal's Algorithm**
Another Greedy algorithm which works on the same principle of selecting the least cost edges available. But there is a difference here. It selects the edges available in such a way that the resulting MST does not form a cycle in it. If it does, then the edge will be discarded.

In order to implement Kruskal's Algorithm, we use the concept of Disjoint Set Union. Here, the nodes belonging to the edges that are added to the MST are considered to be part of a Disjoint Set. Once an edge is added, we check whether the nodes belong to the same subset or not, using the Find operation. If not, we simple unite the two subsets using the Union Operation. If they do, the edge forms a cycle. 

Use Prim's algorithm when the graph is a dense graph. Use Kruskal's algorithm when the graph is sparse.
Kruskal's algorithm runs with a time complexity of O(ElogE) {sorting the edges} where E is the number of edges in the graph.
Prim's algorithm runs with a time complexity of O(ElogV), or even better O(E + VlogV) using a fibonacci heap.

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

### Some points to remember:
- A component with n nodes having an mst will have exactly n - 1 edges.
- To find the number of connected components in a graph you can count the number of edges in a union-find algorithm. At the end, you can subtract n - k (edges) to get the number of connected components in the graph.

'''
2 3 1 0
number of swaps to make permutation resolved = n - 1

3 - 0, 2 - 3, 1 - 2
'''