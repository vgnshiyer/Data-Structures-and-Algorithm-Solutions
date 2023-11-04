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

