#include <bits/stdc++.h>
using namespace std;

const int N = 1000;
const int INF = 1e5;
int n;
int edges[2*N][3];
int dist[N];
int cnt = 0;

/*
Although Djikstra's algorithm gives us the shortest path between two given nodes in O((E+V)LogV), it fails to work in case of a graph with negative edges. In this case, we can use the Bellman Ford Algorithm which uses Dynamic programming to find the shortest path in O(EV) time. The idea is to explore all possible edges for a node. In a graph with n nodes, the longest path from a node can be of at most n - 1 edges. There for n - 1 iterations, we relax every single edge. 

What is relaxation?
- edge(u, v)
if (dist[u] + cost(u, v) < dist[v]){
    dist[v] = dist[u] + cost(u, v) 
}

Algorithm:
1. Mark all initial distances for each node as infinity..
2. for n - 1 times, explore all edges in the graph
3. record all shorter paths to each node for every edge

In case of a complete graph(edge between every pair of nodes), there can be n*(n - 1)/2 edges. The time complexity of Bellman Ford algorithm can be O(n^3) or O(E^2 V)
*/

void add_edge(int u, int v, int w){
    edges[cnt][0] = u;
    edges[cnt][1] = v;
    edges[cnt][2] = w;
    cnt++;
}

void bellmanFord(int src){
    fill(dist, dist + N, INF);
    dist[src] = 0;

    for(int i = 0; i < n-1; i++){
        for(int j = 0; j < cnt; j++){
            if(dist[edges[j][0]] + edges[j][2] < dist[edges[j][1]])
                dist[edges[j][1]] = dist[edges[j][0]] + edges[j][2];
        }
    }

    // check for negative cycles
    for(int i = 0; i < cnt; i++){
        if(dist[edges[i][0]] + edges[i][2] < dist[edges[i][1]]){
            cout << "Graph Contains Negative edge cycle !!\n";
            return;
        }
    }

    cout << "Distance of source \n";
    for(int i = 0; i < n; i++)
        cout << i << " " << dist[i] << "\n";
}

int main(){
    // finding All Pair Shortest path using Floyd Warshall Algorithm (Dynamic Programming)
    // T: O()
    n = 6;
    add_edge(0, 1, 4);
    add_edge(0, 2, 3);
    add_edge(1, 2, 5);
    add_edge(1, 3, 2);
    add_edge(2, 3, 7);
    add_edge(3, 4, 2);
    add_edge(4, 5, 6);
    add_edge(4, 1, 4);
    add_edge(4, 0, 4);

    bellmanFord(0);
    /* OUTPUT
        Distance of source 
        0 0
        1 4
        2 3
        3 6
        4 8
        5 14
    */
}