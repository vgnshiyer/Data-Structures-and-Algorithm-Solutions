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