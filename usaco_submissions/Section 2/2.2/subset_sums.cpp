#include <bits/stdc++.h>
using namespace std;

/*
TASK: subset
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
int ans = 0;

void dbg_dp(vector<vector<int>> dp, int n, int s){
    for(int i = 0; i <= n; i++)
    for(int j = 0; j <= s; j++)
        cout << dp[i][j] << " \n"[j == s];
}

void solve(){
    cin >> n;

    int s = n*(n+1)/2;
    if(s%2) cout << 0 << nline;
    else{   
        s /= 2;
        vector<vector<ll>> dp(n+1, vector<ll>(s+1, 0));
        for(int i = 0; i <= n; i++) dp[i][0] = 1; // creating a sum 0 for any val n has only 1 way

        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= s; j++){
                dp[i][j] = dp[i-1][j];
                if(j-i >= 0)
                    dp[i][j] += dp[i-1][j-i];
            }
        }
        // dbg_dp(dp, n, s);
        cout << dp[n][s]/2 << nline;
    }
}

int main() {
    read_input("subset");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}