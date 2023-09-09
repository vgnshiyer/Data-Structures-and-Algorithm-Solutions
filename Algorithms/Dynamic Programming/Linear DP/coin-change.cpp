#include <bits/stdc++.h>
using namespace std;

/*
The dynamic programming algorithm is based on a recursive function that goes through all possibilities how to form the sum, like a brute force algorithm. However, the dynamic programming algorithm is efficient because it uses memoization and calculates the answer to each subproblem only once.
*/
const int INF = 10000000, N = 10000;
int coins[] = {1,3,4};
vector<int> dp(N, -1);

/* memoized top-down approach
eg. min coins to produce sum of 10
f(10) ==> min(f(9) + 1, f(7)+1, f(6)+1) -- we assume that we have f(9); recursively until we reach the smallest sub problem.

we try with all coins one by one and pick the min value.
*/
int minCoins_recursive(int x){
    if(x == 0) return 0; // 0 coins for 0rs
    if(x < 0) return INF;
    int &ans = dp[x];
    if(ans != -1) return ans;

    int res = INF;
    for(auto coin : coins){
        res = min(res, minCoins_recursive(x-coin)+1);
    }
    return ans = res;
}

/* tabular bottom-up approach
In this approach we start from the base of the tree and compute till the root.

The most basic sub problem in this problem is f(0) = 0;
We construct our dp by using this. 
At the end we return the nth element of the dp matrix.
*/
int minCoins_iterative(int x){
    vector<int> dp(N);
    dp[0] = 0;
    for(int i = 1; i <= x; i++){
        dp[i] = INF;
        for(int coin : coins){
            if(i - coin >= 0){
                dp[i] = min(dp[i],dp[i-coin]+1);
            }
        }
    }
    return dp[x];
}