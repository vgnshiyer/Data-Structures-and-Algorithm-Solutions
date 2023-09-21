#include<bits/stdc++.h>
using namespace std;

class NumMatrix {
private:
    vector<vector<int>> dp;

public:
    NumMatrix(vector<vector<int>>& matrix) {
        int n = matrix.size(), m = matrix[0].size();
        dp.resize(n + 1, vector<int>(m + 1, 0));
        
        for(int i = 1; i <= n; i++)
        for(int j = 1; j <= m; j++)
            dp[i][j] = matrix[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]; // double counting

    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        return dp[row2+1][col2+1] - dp[row2+1][col1] - dp[row1][col2+1] + dp[row1][col1];
    }
};