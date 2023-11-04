### Some Other Important Graph Algorithms worth studying

##### Detecting a cycle in an unidirected graph

given an undirected graph like shown, we need to return whether there is a cycle present in the graph.
```
        0
       / \
      1   2        cycle here is 2->3->4->2 ... 
         / \
        3---4
```

Analysis: O(V+E)
- We maintain one visited array tracks whether the node was visited or not.
- We maintain one parent variable which tracks the node where we came from to a node arrived.
- We explore the current unexplored node.
  - if neighbour is visited, and is equal to the parent, we skip it.
  - if neighbour is unvisited, we call a dfs on that node
  - if node is visited, but is not the parent, We have entered a cycle.

##### Detecting a cycle in a directed graph

given an directed graph like below, return whether there is a cycle present in the graph.
```
                           +---------------+
        0                  |adjacency list:|
       / \                 | 0->1,2        |
      1   2                | 2->3          |
         / \               | 3->4          |
        3---4              | 4->2          | 
                           +---------------+ 
                    cycle here is 2->3->4->2 ... 
```
Analysis:
- Here we cannot use the previous algorithm to detect cycle in an unidirected graph.
- We maintain two arrays, one for visited, and one for the being_explored(rec stack) nodes.
- If we encounter a node which is not visited, we explore it and mark it as visited in our boolean visited array
- If the node is visited and which is being explored, this means that we have entered a cycle. 

