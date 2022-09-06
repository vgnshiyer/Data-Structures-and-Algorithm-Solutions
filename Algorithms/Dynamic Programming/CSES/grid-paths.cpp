#include <bits/stdc++.h>
using namespace std;
 
#define ll long long

const ll MOD = 7 + 1e9;
 
int n;
char grid[1001][1001];
vector<vector<int>> dp(1001, vector<int>(1001, -1));
 
int compute(int i, int j){
    if(grid[i][j] == '*') return 0;
    if(i > n || j > n) return 0;
    if(i == n && j == n) return 1;
 
    if(dp[i][j] != -1) return dp[i][j];
 
    dp[i][j] = compute(i, j+1) + compute(i+1, j);
    dp[i][j] %= MOD;
    return dp[i][j];
}
 
void solve(){
    cin >> n;
    for(int i = 1; i <= n; i++){
        string s; cin >> s;
        for(int j = 1; j <= n; j++)
            grid[i][j] = s[j-1];
    }
 
    cout << compute(1, 1) << endl;
}
 
int main() {
    solve();
    return 0;
}