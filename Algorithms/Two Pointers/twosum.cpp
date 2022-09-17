#include <bits/stdc++.h>
using namespace std;

vector<int> twoSum(vector<int>& numbers, int target) {
    // two pointer approach
    vector<int> res;
    int lo = 0, hi = numbers.size()-1;
    while(lo < hi) {
        int sum = numbers[lo] + numbers[hi];
        if( sum == target) return {lo+1,hi+1};
        else if(sum > target) hi -= 1;
        else lo += 1;
    }
    return {};
    
}