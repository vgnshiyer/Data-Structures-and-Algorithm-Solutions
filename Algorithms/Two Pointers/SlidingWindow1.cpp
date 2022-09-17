#include <bits/stdc++.h>
using namespace std;

// fixed window length
void subarrayWithMaxSum(){
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

// better implementation with single pointer
void maxWindowSum(){
    int sum = 0;
    for(int i = 0; i < window_len; i++) sum += arr[i];
    int max_sum = sum;

    for(int i = 1; i < n-window_len; i++){
        sum -= arr[i-window_len-1];
        sum += arr[i+window_len-1];
        max_sum = max(max_sum, sum);
    }
}

int main(){
    int n; cin >> n;
    vector<int> a(n);
    int k; cin >> k;
    for(int i = 0; i < n; i++) cin>>a[i];
}
