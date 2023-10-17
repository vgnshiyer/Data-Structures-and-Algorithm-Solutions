#include<bits/stdc++.h>
using namespace std;

int numberOfArithmeticSlices(vector<int>& nums) {
    int n = nums.size();
    vector<unordered_map<int, int>> dp(n);

    int ans = 0;
    for (int i = 1; i < n; i++){
        int d = nums[i] - nums[i - 1];
        ans += dp[i - 1][d];
        dp[i][d] += (1 + dp[i - 1][d]);
    }
    
    return ans;
}