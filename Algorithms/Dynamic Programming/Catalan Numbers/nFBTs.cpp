#include <bits/stdc++.h>
using namespace std;

/*Given the value 'n', find the number of ways to construct a full binary tree with n nodes.*/
/*
state: dp[i] => number of ways to construct a FBT with i nodes.
transition: dp[i] => sum(dp[k]dp[i-1-k]) where k ranges from 1 to i-1 (odd vals)
base case: dp[1] = 1;
*/
int dp[10000];

int main(){
    int n = 5;
    dp[1] = 1;
    for(int i = 2; i <= n; i++){
        if(i%2 == 0) continue;
        for(int k = 1; k < i; k+=2)
            dp[i] += dp[k]*dp[i-1-k];
    }
    cout << dp[n] << endl; // nth Catalan number is our final answer
    return 0;
}