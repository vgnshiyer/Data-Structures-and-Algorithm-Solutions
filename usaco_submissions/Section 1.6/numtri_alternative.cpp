#include <bits/stdc++.h>
using namespace std;

/*
TASK: numtri
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long
#define nline "\n"

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

int N;

void solve(){
    cin >> N;
    int triangle[N+1][N+1];
    for(int i = 0; i < N; i++)
    for(int j = 0; j < i+1; j++){
        cin >> triangle[i][j];
    }

    for(int r = N-2; r >= 0; r--)
    for(int c = r; c >= 0; c--)
        triangle[r][c] += max(triangle[r+1][c], triangle[r+1][c+1]);

    cout << triangle[0][0] << nline;
}

int main() {
    read_input("numtri");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}