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
bool being_explored[N];

void add_edge(int x, int y){
    adj_list[x].push_back(y);
}

bool hasCycle(int x){
    visited[x] = true;
    being_explored[x] = true;

    for(int next_node : adj_list[x]){
        if(being_explored[next_node]) return true;
        if(!visited[next_node] && hasCycle(next_node)) return true;
    }
    being_explored[x] = false;
    return false;
}

int main(){
    int n = 5;
    add_edge(0,1);
    add_edge(0,2);
    add_edge(2,3);
    add_edge(3,4);
    add_edge(4,2);

    for(int i = 0; i < n; i++){
        if(hasCycle(i)){
            cout << "We have encountered a cycle in the graph!!!\n";
            return 0;
        }
    }
    cout << "The graph does not have any cycle.\n";
}