#include<bits/stdc++.h>
using namespace std;
   
/*
Reference: https://leetcode.com/problems/maximal-rectangle/solutions/1604254/c-simple-solution-w-explanation-optimizations-from-brute-force-to-dp/?envType=list&envId=rsmzopy7

1. Brute force
 - We try checking the rectangle at every single cell
 - Time complexity: O (NM)^3
*/

int maximalRectangle(vector<vector<char>>& M) {
    if(!size(M)) return 0;
    int ans = 0, m = size(M), n = size(M[0]);
    for(int start_i = 0; start_i < m; start_i++) 
        for(int start_j = 0; start_j < n; start_j++) 
            for(int end_i = start_i; end_i < m; end_i++) 
                for(int end_j = start_j; end_j < n; end_j++) {
                    bool allOnes = true;
                    for(int i = start_i; i <= end_i && allOnes; i++) 
                        for(int j = start_j; j <= end_j && allOnes; j++) 
                            if(M[i][j] != '1') allOnes = false;                           
                    ans = max(ans, allOnes * (end_i - start_i + 1) * (end_j - start_j + 1));
                }
    return ans;
}

/*
2. Optimized Brute force
 - Instead of checking the entire rectangle, we try checking the minimum breadth of the rectangle from a cell towards the right
 - For the row we go as far as we can until we hit the first '0'
 - area = (r - i + 1) * breadth
 - Time complexity: O (NM)^2
*/

int maximalRectangle(vector<vector<char>>& M) {
    if(!size(M)) return 0;
    int ans = 0, m = size(M), n = size(M[0]);
    for(int i = 0; i < m; i++) 
        for(int j = 0; j < n; j++) 
            for(int row = i, breadth = n, col; row < m && M[row][j] == '1'; row++) {
                for(col = j; col < n && M[row][col] == '1'; col++);
                breadth = min(breadth, col-j);
                ans = max(ans, (row-i+1) * breadth);
            }
    return ans;
}

/*
3. DP
 - Precompute the values for the minimum breadth at any position (i, j)
 - For each cell, we try to find the maximum area rectangle that can be formed with the minimum breadth at that cell
 - This reduces one more loop.
 - Time complexity: O (N^2 M)
*/

int maximalRectangle(vector<vector<char>>& M) {
    int n = M.size(), m = M[0].size();
    vector<vector<int>> dp(n+1, vector<int>(m+1, 0));

    for (int i = n-1; i >= 0; i--)
    for (int j = m-1; j >= 0; j--) dp[i][j] = M[i][j] == '1' ? dp[i][j+1] + 1 : 0;

    int ans = 0;
    for(int i = 0; i < n; i++) 
        for(int j = 0; j < m; j++) 
            for(int r = i, breadth = m; r < n && M[r][j] == '1'; r++) {
                breadth = min(breadth, dp[r][j]);
                ans = max(ans, (r-i+1) * breadth);
            }
    return ans;
}

/*
4. DP + monotonic stack
 - We can eliminate one more loop to find the number of rows that have the same breadth at a cell
 - we maintain two matrices up and down which specify the number of rows that have the same breadth at a cell
 - we use the computed dp matrix along with monotonic stack to compute up[i][j] and down[i][j]
    - Time complexity: O (NM)
*/

int maximalRectangle(vector<vector<char>>& M) {
    int ans = 0, n = M.size(), m = M[0].size();
    vector<vector<int>> dp(n+1, vector<int>(m + 1, 0)), up(n+1, vector<int>(m+1, 0)), down(n+1, vector<int>(m+1, 0));

    for (int i = n-1; i >= 0; i--)
    for (int j = m-1; j >= 0; j--) dp[i][j] = M[i][j] == '1' ? dp[i][j+1] + 1 : 0;

    stack<int> s;
    for (int j = 0; j < m; j++) {
        for (int i = 0; i < n; i++){
            while (s.size() && dp[s.top()][j] >= dp[i][j]) s.pop();
            up[i][j] = s.size() ? i - s.top() : i + 1;
            s.push(i);
        }
        s = stack<int>();
        for (int i = n-1; i >= 0; i--){
            while (s.size() && dp[s.top()][j] >= dp[i][j]) s.pop();
            down[i][j] = s.size() ? s.top() - i : n - i;
            s.push(i);
        }
    }

    for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++)
        ans = max(ans, (up[i][j] + down[i][j] - 1) * dp[i][j]);
    return ans;
}

