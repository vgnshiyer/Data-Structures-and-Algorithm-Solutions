## Graph data structure

A graph data structure consists of a finite set of nodes and a finit set of edges. 
These edges can either be directed or undirected and weighted or unweighted.

They are used to represent many real life scenarios. For example, a social network on facebook, can
be represented with the help of an undirected graph. The reason it is undirected is because friendship is 
a mutual relationship. An example of directed relationship is followers on instagram.
Graphs can be used to represent a map, a telephone network, etcetera.

There are two ways to represent a graph:

* adjacency matrix
* adjacency lists

The choice of either of them depends on a mutitude of factors and the pros and cons of both will be discussed below.

#### Adjacency Matrix

In order to represent a graph in the form of a matrix, we allocate a space of N x N 2D array,
where N is the number of nodes in the graph. 
for eg. 
```
   0 1 2 3 4
0| 0 1 0 1 0
1| 1 0 1 0 1 
2| 0 1 0 0 1
3| 1 0 0 0 0
4| 0 1 1 0 0
```
A 1 represents an undirected edge.

**Pros**
1. Easier to implement.
2. Basic queries take O(1) time.
**Cons**
1. Consumes too much space. O(V*V)
2. Stores unnecessary information. (info of no edge between nodes is also stored)

**Implementation**
```
int main(){
    // n: number of nodes, m: number of edges
    int n, m;
    cin >> n >> m;
    int adj_mat[n+1][n+1];
    for(int i = 0; i < m; i++>){
        int u, v;
        cin >> u >> v;
        adj_mat[u][v] = 1;
        adj_mat[v][u] = 1; // undirected graph
    }
}
```

#### Adjacency Lists

The Adjacency list is the other most used form of representations of graphs. The size of the list is equal to the number of nodes in the graph. Every node is allocated its own list to represent a path from the node to the nodes it is connected to (adjacent nodes).
For eg.
```
0 -> 1 -> 3
1 -> 0 -> 3 -> 2
2 -> 1 -> 3
3 -> 1 -> 2 -> 0
```
**Pros**
1. Saves a lot of space. O(V + E)
2. Adding a vertex is easier.
**Cons**
1. Queries can be time consuming. Finding an edge here is O(E) in the worst case.

Despite the cons of adjaceny lists of time complexity, it is much more efficient than storing a graph in an adjacency matrix. Consider an example of a social network, where there could be 10^9 nodes in the network. Allocating a space of 10^18 would be several PB's. Moreover, a node in the network would be hardly connected to around 1000 nodes. So, the network would be a sparse one. Allocating such a big amount of space for such a sparse graph is not feasible. 

Using an adjacency list in such a scenario would be a great choice. Although the time complexity of finding edges may increase, considering the space we are saving, it's a happy compromise.

**Implementation**
```
int main(){
    int n, m;
    cin >> n >> m;
    vector<int> adj_list[1e5];
    for(int i = 0; i < m; i++){
        int x, y; cin >> x >> y;
        adj_list[x].push_back(y);
        adj_list[y].push_back(x);
    }
}
```
