#include <bits/stdc++.h>
using namespace std;

// Kadane's algo
/*
Kadane's algo is a technique in dynamic programming to solve problems of below type
1. find a subarray with a sum
2. maximize or minimize the sum.

Consider a problem of finding a subarray with maximum sum

{1, -1, 2, 3, -4}
       |-ans-|

Basic idea to use in kadane's algo is:
local_maximum at index i is the maximum of A[i] and the sum of A[i] and local_maximum at index i-1.

local_maximum at index i tells us the maximum sum we can get by adding the current bit in the subarray
*/

int getLongestSum(vector<int> arr){
    int n = arr.size();
    int local_max = 0, global_max = INT_MIN;
    for(int i = 0; i < n; i++){
        local_max = max(arr[i], arr[i] + local_max);
        global_max = max(local_max, global_max);
    }
    return global_max;
}

int main(){
    vector<int> arr = {1,-1,2,3,-4};
    cout<<getLongestSum(arr);
    return 0;
}