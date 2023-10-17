#include <bits/stdc++.h>
using namespace std;
 
#define ll long long

const ll MOD = 7 + 1e9;
 
int n;
char grid[1001][1001];
vector<vector<int>> dp(1001, vector<int>(1001, -1));
 
// top-down recursive
int compute(int i, int j){
    if(grid[i][j] == '*') return 0;
    if(i >= n || j >= n) return 0;
    if(i == n-1 && j == n-1) return 1;
 
    if(dp[i][j] != -1) return dp[i][j];
 
    dp[i][j] = compute(i, j+1) + compute(i+1, j);
    dp[i][j] %= MOD;
    return dp[i][j];
}

int compute_iterative() {
    vector<vector<int>> dp(1001, vector<int>(1001, 0));
    dp[0][0] = 1;
    for(int i = 0; i < n; i++)
    for(int j = 0; j < n; j++){
        if(grid[i][j] == '*'){
            dp[i][j] = 0;
            continue;
        }
        if(i) dp[i][j] = dp[i-1][j];
        if(j) dp[i][j] += dp[i][j-1];
    }
    return dp[n-1][n-1];
}
 
void solve(){
    vector<string> gridStrings = {".*..",
                                  ".**.",
                                  "....",
                                  "*..."};
    n = 4;

    for(int i = 0; i < n; i++){
        string s = gridStrings[i];
        for(int j = 0; j < n; j++)
            grid[i][j] = s[j];
    }
 
    cout << compute(0, 0) << endl;
    cout << compute_iterative() << endl;

    // for(int i = 0; i < n; i++)
    // for(int j = 0; j < n; j++){
    //     cout << dp[i][j] <<" \n"[j==n-1];
    // }
}
 
int main() {
    solve();
    return 0;
}