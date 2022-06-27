#include <bits/stdc++.h>
using namespace std;

// finds max window size with sum == s
// dynamic window size problem template
void maxWindowLen(){
    int n, s;
    cin >> n >> s;
    int a[n];
    for(int i = 0; i < n; i++) cin >> a[i];

    int lo = 0, hi = 0, currSum = 0, currLen = INT_MIN;
    for(hi = 0; hi < n; hi++){
        currSum += a[hi];
        while(currSum > s){
            currSum -= a[lo++];
        }
        if(currSum == s) currLen = max(currLen, hi - lo + 1);
    }
    cout <<(currLen == INT_MIN ? -1 : n-currLen)<<endl;
}