#include <bits/stdc++.h>
using namespace std;

/*
    0
   / \
  1   2        GRAPH used to demonstrate the algo
     / \
    3---4
*/

const int N = 1e5;
vector<int> adj_list[N];
bool visited[N];

void add_edge(int x, int y){
    adj_list[x].push_back(y);
    adj_list[y].push_back(x);
}

bool hasCycle(int x, int parent){
    visited[x] = true;

    for(int next_node : adj_list[x]){
        if(visited[next_node] && next_node != parent) return true;
        if(!visited[next_node]) if(hasCycle(next_node, x)) return true;
    }
    return false;
}

int main(){
    int n = 5;
    add_edge(0,1);
    add_edge(0,2);
    add_edge(2,3);
    add_edge(2,4);
    add_edge(3,4);

    if(hasCycle(0, -1)) cout << "We have encountered a cycle in the graph!!!\n";
    else cout << "The graph does not have any cycle.\n";
}