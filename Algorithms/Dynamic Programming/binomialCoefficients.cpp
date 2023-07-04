#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> dp(1000, vector<int>(1000, -1));

int binomialCoeff(int i, int j){
    if(i < 0 || j < 0) return 0;
    if(i == 0 || i == j) return 1;

    if(dp[i][j] == -1) dp[i][j] = binomialCoeff(i-1,j-1) + binomialCoeff(i-1,j);
    return dp[i][j];
}

int binomialCoeff_bottom_up(int n, int k){
    vector<vector<int>> dp2(1000, vector<int>(1000, 0));
    
    // At every iteration for `i`, we calculate choose(i, 0) to choose(i, i)
    dp2[0][0] = 1;
    for(int i = 1; i <= n; i++){
        for(int j = 0; j <= i; j++){
            dp2[i][j] = dp2[i-1][j];
            if(j) dp2[i][j] += dp2[i-1][j-1];
        }
    }
    return dp2[n][k];
}

int main(){
    int n = 5, k = 3;

    cout << binomialCoeff(n, k) << endl;
    cout << binomialCoeff_bottom_up(n, k) << endl;
    return 0;
}