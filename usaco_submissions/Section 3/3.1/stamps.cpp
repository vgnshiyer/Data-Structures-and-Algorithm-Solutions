#include <bits/stdc++.h>
using namespace std;

/*
TASK: stamps
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long
#define nline "\n"

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

int K, N;
int stamps[51];

void solve(){
    cin >> K >> N;
    int mx = -1;
    for(int i = 0; i < N; i++){
        cin >> stamps[i];
        mx = max(mx, stamps[i]);
    }

    vector<int> dp(mx*K, 0);
    dp[0] = 0; // there is always a way to make a sum of zero with zero stamps

    int i = 1;
    for(;;i++){
        dp[i] = INT_MAX;
        for(int s : stamps){
            if(i - s >= 0)
                dp[i] = min(dp[i], 1 + dp[i-s]);
        }
        if(dp[i] > K) break;
    }

    cout << i-1 << nline;
}

int main() {
    read_input("stamps");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}