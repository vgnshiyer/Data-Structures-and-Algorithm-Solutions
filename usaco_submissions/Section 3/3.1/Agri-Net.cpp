#include <bits/stdc++.h>
using namespace std;

/*
TASK: agrinet
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long
#define nline "\n"

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

int n;
int adj_mat[101][101];
bool visited[101];
int min_cst = 0;

struct compare{
    bool operator()(pair<int, int> a, pair<int, int> b){ return a.second > b.second; }
};

void prims(int src){
    priority_queue<pair<int, int>, vector<pair<int, int>>, compare> pq;
    pq.push({src, 0});

    while(!pq.empty()){
        auto p = pq.top();
        pq.pop();
        int node = p.first, weight = p.second;

        if(visited[node]) continue;
        min_cst += weight;
        visited[node] = true;
        for(int i = 0; i < n; i++){
            if(visited[i]) continue;
            pq.push({i, adj_mat[node][i]});
        }
    }
}

void solve(){
    cin >> n;
    for(int i = 0; i < n; i++)
    for(int j = 0; j < n; j++)
        cin >> adj_mat[i][j];
    
    prims(0);
    cout << min_cst << nline;
}

int main() {
    read_input("agrinet");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}