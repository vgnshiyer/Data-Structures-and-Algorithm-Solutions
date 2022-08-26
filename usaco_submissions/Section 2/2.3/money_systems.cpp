#include <bits/stdc++.h>
using namespace std;

/*
TASK: money
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long
#define nline "\n"

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

ll v, n;
ll dp[10001];

void solve(){
    cin >> v >> n;
    dp[0] = 1;
    for(ll i = 0; i < v; i++){
        ll c; cin >> c;
        for(ll s = c; s <= n; s++)
            dp[s] += dp[s-c];
    }
    cout << dp[n];
}

int main() {
    read_input("money");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}