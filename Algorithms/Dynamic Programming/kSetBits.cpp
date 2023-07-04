#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> dp(1000, vector<int>(1000, -1));

int NwaysWithExactlyKSetBits(int n, int k){
    if(n < 0 || k < 0) return 0;
    if(n == 0 || k == n) return 1;
    //                selected a 1      selected a 0  --> for this position (adding all ways)
    if(dp[n][k] != -1) return dp[n][k];
    return dp[n][k] = NwaysWithExactlyKSetBits(n-1, k-1) + NwaysWithExactlyKSetBits(n-1, k);
}

int NwaysWithAtMostKSetBits(int n, int k){
    if(n == 0 || k == 0) return 1; // notice we don't stop at n == k.. if we ran out of places to place k 1's, we can still place 0's
    if(dp[n][k] != -1) return dp[n][k];
    return dp[n][k] = NwaysWithAtMostKSetBits(n-1,k-1) + NwaysWithAtMostKSetBits(n-1,k);
}

int NwaysWithAtMostKSetBits_BottomUp(int n, int k){
    vector<vector<int>> dp2(1000, vector<int>(1000, 0));

    for(int i = 0; i <= n; i++) dp2[i][0] = 1;
    for(int j = 0; j <= k; j++) dp2[0][j] = 1;

    for(int i = 1; i <= n; i++)
    for(int j = 0; j <= k; j++){
        dp2[i][j] = dp2[i-1][j];
        if(j) dp2[i][j] += dp2[i-1][j-1];
    }
    return dp2[n][k];
}

int main(){
    int n = 5, k = 3;

    // cout << NwaysWithExactlyKSetBits(n, k); // Equivalent to choose(5, 3) = 10
    
    cout << NwaysWithAtMostKSetBits(n, k); // Equivalent to {5C3 + 5C2 + 5C1 + 5C0} // 26
    // cout << NwaysWithExactlyKSetBits(5,3) + NwaysWithExactlyKSetBits(5,2) + NwaysWithAtMostKSetBits(5,1) + NwaysWithAtMostKSetBits(5,0) << endl; // prints 26
}