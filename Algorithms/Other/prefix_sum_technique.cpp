#include <bits/stdc++.h>
using namespace std;

// using prefix sum array you can compute the sum of a range in O(1) time
/*
consider a problem where you want to compute the sum of multiple ranges in the array
Having the sum of prefixes allows you to get the sum of a range by just subtracting 
a[r] - a[l] if(l != 0)
*/
int sum_of_range(int l, int r, int p[]){
    return p[r] - (l ? p[l-1] : 0);
}

int main(){
    int n; 
    int a[n], p[n];
    for(int i = 0; i < n; i++){
        cin>>a[i];
        p[i] = a[i];
        if(i) p[i] += p[i-1];
    }
    return 0;
}