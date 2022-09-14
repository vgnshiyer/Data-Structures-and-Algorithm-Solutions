#include <bits/stdc++.h>
using namespace std;

/*
TASK: inflate
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long
#define nline "\n"

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

int m, n;
vector<int> points, minutes;

void solve(){
    cin >> m >> n;
    points.resize(n), minutes.resize(n);
    for(int i = 0; i < n; i++) cin >> points[i] >> minutes[i];

    vector<int> dp(m+1, 0);
    for(int i = 1; i <= n; i++)
    for(int j = minutes[i-1]; j <= m; j++){
        dp[j] = max(dp[j], points[i-1] + dp[j - minutes[i-1]]);
    }

    cout << dp[m] << nline;
}

int main() {
    read_input("inflate");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}