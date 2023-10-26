#include <bits/stdc++.h>
using namespace std;

/*
For performing a topological sort, you always need to start at a node which has an indegree of 0. (meaning, it has not incoming edges)

Main differences between DFS and BFS for topological sorting
- DFS inserts a node in the ordering when the outdegree of the node becomes 0.
- BFS inserts a node in the ordering when the indegree of the node becomes 0.

    0
   / \
  1   2        GRAPH used to demonstrate the algo
     / \
    3   4
*/

const int N = 1e5;
vector<int> adj_list[N];
bool visited[N];
vector<int> order;

void add_edge(int x, int y){
    adj_list[x].push_back(y);
}

void topSort(int x){
    visited[x] = true;

    for(int nxt : adj_list[x]){
        if(visited[nxt]) continue;
        topSort(nxt);
    }
    order.push_back(x);
}

/* Kahn's algorithm to find topological ordering using BFS */
void topSort_BFS(int n) {
    vector<int> indegree = vector<int>(n, 0);
    for(int i = 0; i < n; i++) {
        for(int nxt : adj_list[i]) {
            indegree[nxt]++;
        }
    }

    queue<int> q;
    for(int i = 0; i < n; i++) 
        if (indegree[i] == 0) q.push(i); // push all root nodes
        
    while (!q.empty()){
        int node = q.front();
        q.pop();
        order.push_back(node);
        for (auto nxt : adj_list[node]) {
            indegree[nxt]--;
            if (indegree[nxt] == 0) q.push(nxt);
        }
    }
}

int main(){
    int n = 5;
    add_edge(1,0);
    add_edge(0,2);
    add_edge(2,3);
    add_edge(2,4);

    for(int i = 0; i < n; i++)
        if(!visited[i]) topSort(i);

    // topSort_BFS(n);

    cout << "The topological ordering of the above graph is: \n";
    for(int node : order) cout << node << " "; // 1 3 4 2 0
}