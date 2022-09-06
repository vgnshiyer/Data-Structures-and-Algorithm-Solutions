#include <bits/stdc++.h>
using namespace std;

int n = 7, h = 4;
int dp[205][105];

/*
state: dp[i][j] => # of ways to make a tree with i nodes and height j
transition: dp[i][j] = sum(dp[h][j-1]*dp[i-1-h][j-1]) for all h = 1 to i
base case: dp[1][anything] = 1 if(i%2 == 0) dp[i][anything] = 0
*/

int main(){
    for(int i = 1; i <= n; i += 2)
    for(int j = 1; j <= h; j++){
        if(i == 1) dp[i][j] = 1;
        else{
            for(int x = 1; x < i; x += 2)
                dp[i][j] += dp[x][j-1]*dp[i-1-x][j-1];
        }
    }
    cout << dp[n][h] - dp[n][h-1] << endl;
}