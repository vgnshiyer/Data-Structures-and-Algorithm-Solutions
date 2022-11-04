#include <bits/stdc++.h>
using namespace std;

/*
TASK: game1
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
int dp[102][102];
int sum[102];

void dbg(){
    for(int i = 1; i <= N; i++)
    for(int j = 1; j <= N; j++)
        cout << dp[i][j] << " \n"[j==N];
}

void solve(){
    /* Input */
    cin >> N;
    for(int i = 1; i <= N; i++){
        cin >> dp[i][i];
        sum[i] = sum[i-1] + dp[i][i];
    }

    /* Main routine */
    for(int i = N; i >= 1; i--)
    for(int j = i; j <= N; j++){
        dp[i][j] = sum[j] - sum[i-1] - min(dp[i+1][j], dp[i][j-1]);
    }

    /* debug routine */
    // dbg();

    int score1 = dp[1][N], score2 = sum[N] - dp[1][N];

    cout << score1 << " " << score2 << nline;
}

int main() {
    read_input("game1");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}