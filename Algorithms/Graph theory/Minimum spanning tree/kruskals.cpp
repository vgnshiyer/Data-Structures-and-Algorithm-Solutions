#include <bits/stdc++.h>
using namespace std;

const int N = 1000;
int parent[N];
pair<int, pair<int, int>> edges[N];
int v, n;
int edge_count = 0;
vector<int> size;

void add_edge(int u, int v, int w, int i){
    edges[i] = {w, {u,v}};
}

int collapsive_find(int a){
    // finds parent of subset this node belongs to
    while(parent[a] != a){
        parent[a] = parent[parent[a]]; // collapsive find operation
        a = parent[a];
    }
    // recursive
    // if(parent[a] != a){
    //     parent[a] = collapsive_find(parent[a]);
    //     a = parent[a];
    // }
    return a;
}

void weighted_union(int a, int b){
    int d = collapsive_find(a);
    int e = collapsive_find(b);
    parent[d] = parent[e]; // merge two subsets
    size[e] += size[d] // notice that e and d are swapped
    edge_count++;
}

int KruskalsMST(int n){
    int a, b;
    int cost, minCst = 0;
    for(int i = 0; i < v; i++){
        a = edges[i].second.first;
        b = edges[i].second.second;
        cost = edges[i].first;
        if(collapsive_find(a) != collapsive_find(b)){ // check if we are forming a cycle (both nodes belong to same subset)
            minCst += cost;
            weighted_union(a, b);
        }
    }
    
    cout << "Number of connected components: " << n - edge_count << endl;
    cout << "Size of each component: " << endl;
    
    for(int i = 0; i < n; i++) {
        if (i == parent[i]) {
            cout << size[i] << endl;
        }
    }
    return minCst;
}

int main(){
    n = 6, v = 9;
    add_edge(0, 1, 4, 0);
    add_edge(0, 2, 3, 1);
    add_edge(1, 2, 5, 2);
    add_edge(1, 3, 2, 3);
    add_edge(2, 3, 7, 4);
    add_edge(3, 4, 2, 5);
    add_edge(4, 5, 6, 6);
    add_edge(4, 1, 4, 7);
    add_edge(4, 0, 4, 8);
    sort(edges, edges+v);

    for(int i = 0; i < n; i++) parent[i] = i;
    size.resize(n, 1);

    cout << "Cost of minimum spanning tree from node 0 is : " << KruskalsMST(n) << endl; // 17
    return 0;
}