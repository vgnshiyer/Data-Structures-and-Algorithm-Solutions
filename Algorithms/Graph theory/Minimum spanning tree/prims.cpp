#include <bits/stdc++.h>
using namespace std;

const int N = 1000;
int n;
vector<pair<int, int>> adj_list[N]; 
bool visited[N]; // boolean array to tell if a node was visited or not

void add_edge(int u, int v, int w){
    adj_list[u].push_back({v,w});
    adj_list[v].push_back({u,w});
}

struct compare{
    bool operator()(pair<int, int> a, pair<int, int> b){ return a.second > b.second; }
};

int Prims(int src){
    priority_queue<pair<int, int>, vector<pair<int, int>>, compare> pq;
    pq.push({src, 0});

    fill(visited, visited+n, false);
    int mst_cost = 0;
    
    while(!pq.empty()){
        auto p = pq.top();
        pq.pop();
        int node = p.first;
        int cost = p.second;

        if(visited[node]) continue;
        mst_cost += cost;
        visited[node] = true;

        // Iterate through all the adjacent nodes of the node
        // push the adjacent nodes in the pq only if they are not visited yet
        for(auto next : adj_list[node]){
            int adj_node = next.first;
            if(!visited[adj_node]) pq.push(next);
        }
    }
    return mst_cost;
}

int main(){
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

    cout << "Cost of minimum spanning tree from node 0 is : " << Prims(0) << endl; // 17
    return 0;
}