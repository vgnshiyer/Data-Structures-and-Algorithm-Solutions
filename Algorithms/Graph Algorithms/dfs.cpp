#include <bits/stdc++.h>
using namespace std;

const int N = 1e5;
vector<int> adj_list[N];
bool visited[N];

void add_edge(int x, int y){
    adj_list[x].push_back(y);
    adj_list[y].push_back(x);
}

void DFS(int x){
    visited[x] = true;
    cout << x << " ";

    for(int next_node : adj_list[x]){
        if(visited[next_node]) continue;
        DFS(next_node);
    }
}

int main(){
    int n = 7;
    add_edge(0,1);
    add_edge(0,2);
    add_edge(1,2);
    add_edge(2,0);
    add_edge(2,3);
    add_edge(3,1);

    add_edge(4,5);
    add_edge(4,6);
    DFS(2); // 2 0 1 3 

    // printing total number of connected components
    int ans = 0;
    for(int i = 0; i < n; i++){
        if(visited[i]) continue;
        DFS(i); 
        ans++;
    }
    cout << "Connected components in the graph: " << ans;

    return 0;
}