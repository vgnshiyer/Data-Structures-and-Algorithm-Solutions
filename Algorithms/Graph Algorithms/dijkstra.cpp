#include <bits/stdc++.h>
using namespace std;

const int N = 1000;
int n;
vector<pair<int, int>> adj_list[N]; 
bool visited[N]; // boolean array to tell if a node was visited or not
int dist[N]; // shortest distance of node from the given source

void add_edge(int u, int v, int w){ adj_list[u].push_back({v, w}); }

struct compare{
    bool operator()(pair<int, int> a, pair<int, int> b){ return a.second > b.second; }
};

void dijkstra(int src){
    priority_queue<pair<int, int>, vector<pair<int, int>>, compare> pq;
    pq.push({src, 0});
    dist[src] = 0;

    while(!pq.empty()){
        auto parent = pq.top();
        pq.pop();
        if(dist[parent.first] < parent.second) continue;
        for(auto child : adj_list[parent.first]){
            if(visited[child.first]) continue;
            int newDist = dist[parent.first] + child.second;
            if(newDist < dist[child.first]){
                dist[child.first] = newDist;
                pq.push({child.first, dist[child.first]});
            }
        }
        visited[parent.first] = true;
    }
}

int main(){
    // finding All Pair Shortest path using Dijkstra's Algorithm (Greedy)
    // T: O((E+N)*Log(V))
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

    for(int i = 0; i < n;i ++){
        fill(dist, dist + N, 1e5);
        fill(visited, visited + N, false);
        dijkstra(i);
        cout << "shortest path from node " << i << " to every other node:\n";
        for(int j = 0; j < n; j++) cout << dist[j] << " \n"[j == n-1];
    }
    /* OUTPUT:
        shortest path from node 0 to every other node:
        0 4 3 6 8 14
        shortest path from node 1 to every other node:
        8 0 5 2 4 10
        shortest path from node 2 to every other node:
        13 13 0 7 9 15
        shortest path from node 3 to every other node:
        6 6 9 0 2 8
        shortest path from node 4 to every other node:
        4 4 7 6 0 6
        shortest path from node 5 to every other node:
        100000 100000 100000 100000 100000 0
    */
}