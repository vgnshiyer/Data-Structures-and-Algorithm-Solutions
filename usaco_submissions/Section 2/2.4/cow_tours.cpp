#include <bits/stdc++.h>
using namespace std;

/*
TASK: cowtour
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long
#define nline "\n"
#define F first
#define S second
#define sq(x) x*x
typedef pair<int, int> pii;

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

int n;
const double INF = 1e6;
vector<vector<double>> adj_mat;
vector<pii> pos;

double get_distance(pii a, pii b){
    int x = (a.F - b.F), y = (a.S - b.S);
    return sqrt(sq(x) + sq(y));
}

void solve(){
    cin >> n;
    pos.resize(n);
    adj_mat.resize(n, vector<double>(n, 0));
    for(int i = 0; i < n; i++) cin >> pos[i].F >> pos[i].S;

    for(int i = 0; i < n; i++)
    for(int j = 0; j < n; j++){
        char c; cin >> c;
        int p = c - '0';
        if(p) adj_mat[i][j] = get_distance(pos[i], pos[j]);
        else adj_mat[i][j] = INF;

        if(i == j) adj_mat[i][j] = 0;
    }

    /* Floyd Warshall  all pair shortest paths*/
    for(int k = 0; k < n; k++)
    for(int i = 0; i < n; i++)
    for(int j = 0; j < n; j++)
        adj_mat[i][j] = min(adj_mat[i][j], adj_mat[i][k] + adj_mat[k][j]);

    double diam[n];
    double global_max = -1;
    for(int i = 0; i < n; i++){
        diam[i] = -1;
        for(int j = 0; j < n; j++){
            if(adj_mat[i][j] == INF) continue;
            diam[i] = max(diam[i], adj_mat[i][j]);
        }
        global_max = max(global_max, diam[i]);
    }
    double ans = INF;
    for(int i = 0; i < n; i++)
    for(int j = 0; j < n; j++){
        if(adj_mat[i][j] != INF) continue;
        ans = min(ans, diam[i] + get_distance(pos[i], pos[j]) + diam[j]);
    }
    cout << (global_max > ans ? global_max : ans) << nline; // what if there was some diameter bigger, even before adding the edges to join the pastures
}

int main() {
    read_input("cowtour");
    cout << fixed;
    cout << setprecision(6);
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}