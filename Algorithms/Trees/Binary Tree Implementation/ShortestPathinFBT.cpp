/*
Consider an infinite full binary tree (each node has two children except the leaf nodes) defined as follows. For a node labelled v its left child will be labelled 2*v and its right child will be labelled 2*v+1. The root is labelled as 1.

You are given N queries of the form i j. For each query, you have to print the length of the shortest path between node labelled i and node labelled j.

ANALYSIS: We trace the path from both the nodes to their lowest common ancestor. -> shortest path to each other.

We divide the greater number by 2 at every step and count the number of steps. Therefore the answer is least number of steps that makes both nodes same.
*/

#include <bits/stdc++.h>
using namespace std;

ll dist(ll a, ll b){
    if(a == b) return 0;

    if(a > b) swap(a, b);
    return 1 + dist(a, b/2);
}

int main(){
    int n; cin >> n;
    ll x, y;
    for(int i = 0; i < n; i++){
        cin >> x >> y;
        cout << dist(x, y) << nline;
    }
}