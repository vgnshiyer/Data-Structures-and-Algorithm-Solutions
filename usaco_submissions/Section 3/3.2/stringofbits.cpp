#include <bits/stdc++.h>
using namespace std;

/*
TASK: kimbits
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long
#define nline "\n"

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

ll n, l, I;

void solve(){
    cin >> n >> l >> I;
    
    vector<vector<int>> dp(n+1, vector<int>(l+1, 0));
    dp[0][0] = 1;

    for(ll i = 1; i <= n; i++){
        for(ll j = 0; j <= l; j++){
            dp[i][j] = dp[i-1][j];
            if(j > 0){
                dp[i][j] += dp[i-1][j-1];
            }
        }
    }

    // dp[i][j] gives number of ways to form string of i bits with 0 to j 1's.

    for(ll i = 0; i < n; i++){
        ll sum = 0;
        for(ll j = 0; j <= l; j++){
            sum += dp[n-i-1][j];
        }
        if(sum < I){
            I-= sum;
            cout << 1;
            l--;
        } else{
            cout << 0;
        }
    }
    cout << nline;
}   

int main() {
    read_input("kimbits");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}