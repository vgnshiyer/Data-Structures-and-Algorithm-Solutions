#include <iostream>
#include <bits/stdc++.h>
using namespace std;

/*
state: dp[x][i] => number of ways to fill prefix till index i such that current element is x
transition: dp[j][i] = dp[j-1][i-1] + dp[j][i-1] + dp[j+1][i-1]
base case: if(arr[i] != 0 && arr[i] != j) return 0; (dp[i][j] = 0)

What I understood:
 - every index except the first one in the array constraints the number of choices we can make such that the reqd conditions are satisfied for the whole array.
 - for eg. 
  in an array {0, 0, 2}
               ^
               at this index there are 3 ways to select this index {1, 2, 3} becuase in an array with just 1 element, selecting any element will satisfy our condition.
                  ^
                  However, at the second index we discover that our choices get constrained as the we also need to maintain a difference of 1 between the elements.
                     ^ 
                     The last index furthur constraints the number of choices as we cannot change this element now.
dp table: 
  n ->
m 1 2 0
| 1 3 7
  1 2 0               
*/

#define ll long long

const ll MOD = 1e9+7;
ll n, m;
ll arr[100005];
vector<vector<ll>> dp;

ll solve_recursively(ll j, ll i){
  ll &ans = dp[j][i];
  if(ans != -1) return ans;
  if(i < 0 || j <= 0 || j > m) return ans = 0;
  if(i == 0){
    if(arr[i] == 0 || j == arr[i]) return ans = 1;
    return ans = 0;
  }
  if(arr[i] != 0 && arr[i] != j) return ans = 0;
  
  ans = solve_recursively(j-1, i-1) + solve_recursively(j, i-1) + solve_recursively(j+1, i-1);
  ans %= MOD;
  return ans;
}

ll solve_iteratively(){
    vector<vector<ll>> dp2(m+5, vector<ll>(n+5, 0));
    for(int i = 1; i <= m; i++)
        if(i == arr[0] || arr[0] == 0) dp2[i][0] = 1;

    for(int j = 1; j < n; j++)
    for(int i = 1; i <= m; i++){
      if(arr[j] == 0 || arr[j] == i){
        dp2[i][j] = dp2[i][j-1];
        if(i > 1) dp2[i][j] += dp2[i-1][j-1];
        if(i < m) dp2[i][j] += dp2[i+1][j-1];
        dp2[i][j] %= MOD;
      }
    }

    ll sum = 0;
    for(int i = 1; i <= m; i++){
        sum += dp2[i][n-1];
        sum %= MOD;
    }
    
    return sum;
}

void dbg_dp(){
  for(int i = 1; i <= m; i++){
    for(int j = 0; j < n; j++){
      cout << dp[i][j] << " \n"[j == n-1];
    }
  }
}

int main()
{
  cin >> n >> m;
  dp.resize(m+5, vector<ll>(n+5, -1));
  
  for(ll i = 0; i < n; i++) cin >> arr[i];
  ll sum = 0;
  for(ll i = 1; i <= m; i++){
    sum += solve_recursively(i, n-1);
    sum %= MOD;
  }
  cout << sum << endl;

  cout << solve_iteratively() << endl;
  
  // dbg_dp();
  return 0;
}