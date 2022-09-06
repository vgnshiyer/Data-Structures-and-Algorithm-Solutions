#include <bits/stdc++.h>
using namespace std;

// const int N = 1e6;
const long long MOD = 1e9 + 7;
const int INF = INT_MAX;

/*
The main difference between this problem and the previous one is that given a sum s, we had to find all possible ways to solve the problem
Here, We need to determing the unique ways to generate the sum. So, the problem boils down to deciding whether to select a particular coin in the result or not. The order of the coin in the solution does not matter. Therefore the sub problems formed here is:

* If the highest coin does not exceed the required sum. then the number of unique ways of getting sum s is the total number of ways of getting the sum with and without the highest coin.
* If the highest coin is greater than the reqd sum, the answer is equal to the number of ways to solve the problem without the highest coin.
*/

int dp[1000][1000];
int n, s;
vector<int> coins(n);

int min_coins2_recursive(int x, int i){
    if(x == s) return 1;
    if(i >= n) return 0;

    int &ans = dp[x][i];
    if(ans) return ans;
    int res = 0;
    // include ith coin
    if(coins[i] <= s-x)
    res += min_coins2_recursive(x+coins[i], i);
    // exclude ith coin
    res += min_coins2_recursive(x, i+1);
    return ans = res;
}

void min_coins2_iterative(){
    cin >> n >> s;
    for(int &x : coins) cin >> x;

    vector<vector<int>> dp(n+1,vector<int>(s+1,0)); // dp state that defines, given sum s, how many unique ways possible to get a sum with the given coins
    dp[0][0] = 1;
    for(int i = 1; i <= n; i++){
        for(int j = 0; j <= s; j++){
            dp[i][j] = dp[i-1][j]; // excluding current coin
            if(j - coins[i-1] >= 0){ // using 0 based indexing
                dp[i][j] += dp[i][j-coins[i-1]]; // including current coin
                // provided that difference is >= 0
            }
            dp[i][j] %= MOD;
        }
    }
    cout << dp[n][s] ;
}

// space optimized version
void min_coins2_iterative_space_optimized(){
    long long dp[10001];
    dp[0] = 1;

    cin >> n >> s;
    for(int i = 0; i < n; i++){
        long long c; cin >> c;
        for(int j = c; j <= s; j++)
            dp[j] += dp[j-c];
    }
    cout << dp[s];
}

int main() {
    min_coins2_iterative();
    min_coins2_recursive(0,0);
    return 0;
}