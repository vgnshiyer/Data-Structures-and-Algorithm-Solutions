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
int triangle[1000][1000];
vector<vector<int>> dp(1000, vector<int>(1000, -1));

int compute(int r, int c){
    if(r == N) return 0;

    int &ans = dp[r][c];
    if(ans != -1) return ans; // saving recomputation

    return ans = triangle[r][c] + max(compute(r+1, c), compute(r+1, c+1)); // memoization
}

void solve(){
    cin >> N;
    for(int i = 0; i < N; i++)
    for(int j = 0; j < i+1; j++){
        cin >> triangle[i][j];
    }

    int best = compute(0,0);
    cout << best << nline;
}

int main() {
    read_input("numtri");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}