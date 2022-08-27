#include <bits/stdc++.h>
using namespace std;

/*
TASK: concom
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
int explored[101];
int shares[101];

void DFS(int x){
    if(explored[x]) return;
    explored[x] = true;

    for(int y = 1; y <= 100; y++){
        shares[y] += adj_mat[x][y];
        if(shares[y] > 50)
            DFS(y);
    }
}

void solve(){
    cin >> n;
    int x, y, w;
    for(int i = 0; i < n; i++){
        cin >> x >> y >> w;
        adj_mat[x][y] = w;
    }

    for(int x = 1; x <= 100; x++){
        fill(shares, shares+101, 0);
        fill(explored, explored+101, 0);
        DFS(x);
        for(int y = 1; y <= 100; y++)
            if(x != y && shares[y] > 50) cout << x << " " << y << nline;
    }
}

int main() {
    read_input("concom");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}