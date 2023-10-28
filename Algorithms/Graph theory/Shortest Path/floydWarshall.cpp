#include <bits/stdc++.h>
using namespace std;

const int N = 1000;
const int INF = 1e5;
int n;
int adj_mat[N][N];

void init(){
    for(int i = 0; i < n; i++)
    for(int j = 0; j < n; j++)
        i == j ? adj_mat[i][j] = 0 : adj_mat[i][j] = INF;
}

void add_edge(int u, int v, int w){ adj_mat[u][v] = w; }

void floyd_warshall(){
    for(int k = 0; k < n; k++)
    for(int i = 0; i < n; i++)
    for(int j = 0; j < n; j++)
        adj_mat[i][j] = min(adj_mat[i][j], adj_mat[i][k] + adj_mat[k][j]);
}

void display(){
    for(int i = 0; i < n; i++)
    for(int j = 0; j < n; j++)
        cout << adj_mat[i][j] << " \n"[j==n-1];

    cout << "\n";
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

    display();
    floyd_warshall();
    display();

    /* OUTPUT: 
        0 4 3 100000 100000 100000
        100000 0 5 2 100000 100000
        100000 100000 0 7 100000 100000
        100000 100000 100000 0 2 100000
        4 4 100000 100000 0 6
        100000 100000 100000 100000 100000 0

        0 4 3 6 8 14
        8 0 5 2 4 10
        13 13 0 7 9 15
        6 6 9 0 2 8
        4 4 7 6 0 6
        100000 100000 100000 100000 100000 0
    */
}