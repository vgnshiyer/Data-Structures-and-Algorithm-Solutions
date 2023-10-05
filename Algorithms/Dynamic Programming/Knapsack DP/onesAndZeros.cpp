#include <bits/stdc++.h>
using namespace std;

/* Iterative DP */
int findMaxForm(vector<string>& strs, int m, int n) {
    vector<pair<int, int>> mn(strs.size());
    int i = 0;
    for (auto s : strs) {
        int zeros = 0, ones = 0;
        for (char c : s)
            zeros += c == '0', ones += c == '1';
        mn[i++] = {ones, zeros};
    }

    vector<vector<vector<int>>> dp(strs.size() + 1, vector<vector<int>>(m + 1, vector<int>(n + 1, 0)));
    dp[strs.size()][0][0] = 0;

    for (int i = strs.size() - 1; i >= 0; i--) {
        for (int j = m; j >= 0; j--) {
            for (int k = n; k >= 0; k--) {
                dp[i][j][k] = dp[i + 1][j][k];

                int zeros = mn[i].second, ones = mn[i].first;
                if (j >= zeros && k >= ones)
                    dp[i][j][k] = max(dp[i][j][k], 1 + dp[i + 1][j - zeros][k - ones]);
            }
        }
    }
    return dp[0][m][n];
}

/* Iterative space-optimized dp */
int findMaxForm(vector<string>& strs, int m, int n) {
    vector<pair<int, int>> mn(strs.size());
    int i = 0;
    for (auto s : strs) {
        int zeros = 0, ones = 0;
        for (char c : s)
            zeros += c == '0', ones += c == '1';
        mn[i++] = {ones, zeros};
    }

    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
    dp[0][0] = 0;

    for (int i = strs.size() - 1; i >= 0; i--) {
        for (int j = m; j >= 0; j--) {
            for (int k = n; k >= 0; k--) {
                int zeros = mn[i].second, ones = mn[i].first;
                if (j >= zeros && k >= ones)
                    dp[j][k] = max(dp[j][k], 1 + dp[j - zeros][k - ones]);
            }
        }
    }
    return dp[m][n];
}