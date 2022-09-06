#include <bits/stdc++.h>
using namespace std;

bool someCondition = true;

// binary search template -- replace with appropriate condition
int binarySearch(vector<int> a){
    int n = a.size();
    int lo = 0, hi = n;
    while(lo < hi){
        int mid = (lo + hi) >> 1;
        if(someCondition)
            lo = mid+1;
        else
            hi = mid;
    }
    return lo; // or hi as both are same
}