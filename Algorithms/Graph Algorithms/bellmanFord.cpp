#include <bits/stdc++.h>
using namespace std;

const int N = 1000;
const int INF = 1e5;
int n;

void init(){

}

void add_edge(int u, int v, int w){

}

int main(){
    // finding All Pair Shortest path using Floyd Warshall Algorithm (Dynamic Programming)
    // T: O()
    n = 6;
    init();
    add_edge(0, 1, 4);
    add_edge(0, 2, 3);
    add_edge(1, 2, 5);
    add_edge(1, 3, 2);
    add_edge(2, 3, 7);
    add_edge(3, 4, 2);
    add_edge(4, 5, 6);
    add_edge(4, 1, 4);
    add_edge(4, 0, 4);

}