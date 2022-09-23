#include <bits/stdc++.h>
using namespace std;

/*
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
    adj_list[y].push_back(x);
}

void topSort(int x){
    visited[x] = true;

    for(int nxt : adj_list[x]){
        if(visited[nxt]) continue;
        topSort(nxt);
    }
    order.push_back(x);
}

int main(){
    int n = 5;
    add_edge(0,1);
    add_edge(0,2);
    add_edge(2,3);
    add_edge(2,4);

    for(int i = 0; i < n; i++)
        if(!visited[i]) topSort(i);

    cout << "The topological ordering of the above graph is: \n";
    for(int node : order) cout << node << " "; // 1 3 4 2 0
}