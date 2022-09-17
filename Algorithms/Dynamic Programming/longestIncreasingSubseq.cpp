#include <bits/stdc++.h>
using namespace std;

/*
Given a list of numbers, find the longest subsequence in it which is ascending in order.

First let's solve the problem using a basic recursive algorithm to find the LIS.

The Recursive Algorithm: 
- After reaching every element, we decide whether we include this element in our LIS or not.
- if the current element is greater than the previous, then we increase the length of our LIS by 1.
- we check is there a possible longer subsequence by excluding the current element from the sequence,
despite it being greater than the previous element.
*/

// TOP-DOWN Dynamic Programming Approach
vector<vector<int>> dp(1000, vector<int>(1000, -1)); // 2D dp array
int getLIS_recursive(vector<int> a, int n, int i,int prev){
    if(i == n) return 0;

    int &ans = dp[i][prev];
    if(ans != -1) return ans; // saving the recomputation

    int exclude = getLIS_recursive(a, n, i+1, prev);

    int include = 0;
    if(a[i] > prev){
        include = 1 + getLIS_recursive(a, n, i+1, a[i]);
    }
    return ans = max(include, exclude); // memoization
}

// BOTTOM-UP Dynamic Programming Approach
int getLIS_iterative(vector<int> a, int n){
    vector<int> dp2(n);
    dp2[0] = 1;
    int max_val = 1;
    for(int i = 1; i < n; i++){
        dp2[i] = 1;
        for(int j = 0; j < i; j++){
            if(a[i] > a[j]){
                dp2[i] = max(dp2[i], dp2[j]+1);
            }
        }
        max_val = max(max_val, dp2[i]);
    }
    return max_val;
}

int main(){
    cout << "recursive: " << getLIS_recursive({ 3, 2, 6, 4, 5, 1 }, 6, 0, 0) << endl; // 3
    cout << "iterative: " << getLIS_iterative({ 3, 2, 6, 4, 5, 1 }, 6) << endl; // 3
    return 0;
}