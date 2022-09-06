#include <bits/stdc++.h>
using namespace std;

//O(nlogn)
int getAPDiff(vector<int> a){
    sort(a.begin(),a.end());

    int n = a.size();
    if(n==1) return 0;
    int diff = a[1]-a[0];
    for(int i = 2; i < n; i++){
        if(a[i]-a[i-1] != diff) return -1;
    }
    return diff;
}

//Without sorting
//O(n) using hashset
int getAPDiff2(vector<int> a){
    unordered_set<int> hm;
    int n = a.size();
    int maxi = INT_MIN, mini = INT_MAX;
    for(int i= 0; i < n; i++){
        maxi = max(maxi, a[i]);
        mini = min(mini, a[i]);
        hm.insert(a[i]);
    }

    //formula to calculate diff in an Arithmetic Progression
    int diff = (maxi - mini) / n-1;
    int count = 0;

    while(hm.find(maxi) != hm.end()){
        count++;
        maxi -= diff;
    }
    return count==n;
}