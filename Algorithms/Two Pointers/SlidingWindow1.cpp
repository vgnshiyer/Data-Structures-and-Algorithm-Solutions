#include <bits/stdc++.h>
using namespace std;

// fixed window length
void subarrayWithMaxSum(){
    int n; cin >> n;
    vector<int> a(n);
    int k; cin >> k;
    for(int i = 0; i < n; i++) cin>>a[i];

    int ans = INT_MIN;
    int currSum = 0, currLen = 0;
    int lo = 0;
    for(int hi = 0; hi < n; hi++){
        if(currLen == k){
            ans = max(ans, currSum);
            currSum -= a[lo++];
            currLen--;
        }
        currSum += a[hi];
        currLen++;
    }
    cout<<ans<<endl;
}