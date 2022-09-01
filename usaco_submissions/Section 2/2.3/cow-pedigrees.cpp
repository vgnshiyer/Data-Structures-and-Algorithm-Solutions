#include <bits/stdc++.h>
using namespace std;

/*
TASK: nocows
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long
#define nline "\n"

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

int n, k;
int dp[205][105];
const int MOD = 9901;

/*
state: dp[i][j] => # of ways to make a tree with i nodes and height j
transition: dp[i][j] = sum(dp[k][j-1]*dp[i-1-k][j-1]) for all k = 1 to i
base case: dp[1][anything] = 1 if(i%2 == 0) dp[i][anything] = 0
*/

int compute(){
    for(int i = 1; i <= n; i += 2)
    for(int j = 1; j <= k; j++){
        if(i == 1) dp[i][j] = 1;
        else{
            for(int x = 1; x < i; x += 2){
                dp[i][j] += dp[x][j-1]*dp[i-1-x][j-1];
                dp[i][j] %= MOD;
            }
        }
    }
    return (dp[n][k] - dp[n][k-1] + MOD)%MOD;
}

void dbg_dp(){
    for(int i = 1; i <= n; i++)
    for(int j = 1; j <= k; j++)
        cout << dp[i][j] << " \n"[j == k];
}

void solve(){
    cin >> n >> k;
    cout << compute() << nline;
    // dbg_dp();
}

int main() {
    read_input("nocows");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}