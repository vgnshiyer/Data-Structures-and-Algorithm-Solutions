#include <bits/stdc++.h>
using namespace std;

/*Given the value 'n', find the number of ways to construct a binary search tree with n nodes.*/
/*
state: dp[i] => number of ways to construct a BST with i nodes.
transition: dp[i] => sum(dp[k]dp[i-1-k]) where k ranges from 0 to i
base case: dp[0] = dp[1] = 1;
*/
int dp[10000];

int main(){
    int n = 5;
    dp[0] = dp[1] = 1;
    for(int i = 2; i <= n; i++){
        for(int k = 0; k < i; k++)
            dp[i] += dp[k]*dp[i-1-k];
    }
    cout << dp[n] << endl; // nth Catalan number is our final answer
    return 0;
}