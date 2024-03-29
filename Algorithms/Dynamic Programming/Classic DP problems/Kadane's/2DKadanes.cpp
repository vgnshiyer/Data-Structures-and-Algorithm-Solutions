#include<bits/stdc++.h>
using namespace std;

/* Kadane's algorithm for 1D array */
int Kadanes(vector<int>& arr) {
    int maxSum = INT_MIN, curSum = 0;
    for (int x : arr) {
        curSum = max(curSum + x, x);
        maxSum = max(maxSum, curSum);
    }
    return maxSum;
}

/* Kadane's algorithm using divide and conquer approach */
int Kadanes_divide_and_conquer(vector<int>& nums, int l, int r) {
    if (l > r) {
        return INT_MIN;
    }
    int m = l + (r - l) / 2, ml = 0, mr = 0;
    int lmax = Kadanes_divide_and_conquer(nums, l, m - 1); // find left max excluding current element
    int rmax = Kadanes_divide_and_conquer(nums, m + 1, r); // find right max excluding current elemetn
    
    // find max sum including current element
    for (int i = m - 1, sum = 0; i >= l; i--) {
        sum += nums[i];
        ml = max(sum, ml); // finding best sum towards left
    }
    for (int i = m + 1, sum = 0; i <= r; i++) {
        sum += nums[i];
        mr = max(sum, mr); // finding best sum towards right
    }
    return max(max(lmax, rmax), ml + mr + nums[m]); // return max of left, right or sum including current element
}

/* 2D Kadane's algorithm */
int maximalRectangleSum(vector<vector<int>> &matrix) {
    int n = matrix.size(), m = matrix[0].size();
    int maxSum = INT_MIN;
    for (int l = 0; l < m; l++) {
        vector<int> rowSums(m, 0);
        /* try all rectangles from l = 0 to l = m */
        for (int r = l; r < m; r++) {
            /* keep adding the column r to the rowSums to get the rowPrefix sums */
            for (int i = 0; i < n; i++) rowSums[i] += matrix[i][r];

            /* now we have a 1D array of rowSums, we can apply Kadane's algorithm to get the max sum subarray */
            int curMaxSum = Kadanes(rowSums);

            /* update the maxSum */
            maxSum = max(maxSum, curMaxSum);
        }
    }
    return maxSum;
}

int main() {
    vector<vector<int>> matrix = {
        {1, 2, -1, -4, -20},
        {-8, -3, 4, 2, 1},
        {3, 8, 10, 1, 3},
        {-4, -1, 1, 7, -6}
    };

    /*
        Expected Output: 29
    */

    cout << maximalRectangleSum(matrix) << endl;
}
    