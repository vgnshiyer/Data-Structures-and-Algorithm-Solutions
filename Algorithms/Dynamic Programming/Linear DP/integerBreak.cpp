/*
state: dp[i] -> number of ways to get max product for n = i
transition: dp[i] = max(dp[i], j * dp[i-j], j * (i-j)) for j = 1 to i
base case: dp[0] = 0, dp[1] = 0, dp[2] = 1
*/

int integerBreak(int n) {
    vector<int> dp(59, -1);

    dp[0] = 0, dp[1] = 0, dp[2] = 1;

    for (int i = 3; i <= n; i++)
    for (int j = 1; j <= i; j++)
        dp[i] = max({dp[i], j * dp[i-j], j * (i-j)});

    return dp[n];
}