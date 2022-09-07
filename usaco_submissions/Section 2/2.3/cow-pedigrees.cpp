#include <bits/stdc++.h>
using namespace std;

/*
TASK: nocows
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long
#define nline "\n"

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

int n, k;
int dp[205][105];
const int MOD = 9901;

/*
A simpler problem to solve here is finding all possible FBT's with n nodes.
state: dp[i] => ways to make a tree with i nodes
transition: dp[i] = sum(dp[k]*dp[i-1-k]) for all k = 1 to i-1
base case: dp[1] = 1 (only one way to make a tree with 1 node)

Consider the problem for n = x; Number of ways cld be
1)          x  <- selected one node as root
           / \
          1   x-1-1
2)          x
           / \
          3   x-1-3          // Notice that we are skipping the even numbers as a full binary tree with even nodes cannot be formed.
            .
            .
            .
Therefore in the transition, we multiply the number of combinations for the left subtree and the right subtree such that both are FBT's.

Now, in the below problem, we are adding one more parameter which determines the height of the FBT. So we will extend our DP state to maintain one more parameter.

Below is the state and transition for the main problem.
state: dp[i][j] => # of ways to make a tree with i nodes and height j
transition: dp[i][j] = sum(dp[k][j-1]*dp[i-1-k][j-1]) for all k = 1 to i
base case: dp[1][anything] = 1 if(i%2 == 0) dp[i][anything] = 0

in the transition here, we add the combinations for left and right subtree with current height-1 (the 1 being the root node which we select)

at the end, for height k we will be getting the prefix sum for all the heights from 1 to k for node n.
we simply return the val for k - val for k-1
*/

int compute(){
    for(int i = 1; i <= n; i += 2)
    for(int j = 1; j <= k; j++){
        if(i == 1) dp[i][j] = 1;
        else{
            for(int x = 1; x < i; x += 2){
                dp[i][j] += dp[x][j-1]*dp[i-1-x][j-1];
                dp[i][j] %= MOD;
            }
        }
    }
    return (dp[n][k] - dp[n][k-1] + MOD)%MOD;
}

void dbg_dp(){
    for(int i = 1; i <= n; i++)
    for(int j = 1; j <= k; j++)
        cout << dp[i][j] << " \n"[j == k];
}

void solve(){
    cin >> n >> k;
    cout << compute() << nline;
    // dbg_dp();
}

int main() {
    read_input("nocows");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}