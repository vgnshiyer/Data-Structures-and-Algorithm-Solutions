#include <bits/stdc++.h>
using namespace std;

int ternarySearch(vector<int> arr, int tgt){
    int n = arr.size();
    int l = 0, r = n - 1;
    while(l <= r){
        int m1 = l + (r-l)/3;
        int m2 = r - (r-l)/3;

        if(arr[m1] == tgt) return m1;
        if(arr[m2] == tgt) return m2;

        if(tgt > arr[m2]) l = m2 + 1;
        else if(tgt > arr[m1]){
            l = m1 + 1;
            r = m2 - 1;
        }
        else r = m1 - 1;
    }
    return -1;
}

int main(){
    vector<int> arr = {5,6,7,8,4,3,2,1};
    int tgt = 6;
    cout << ternarySearch(arr, tgt) << endl;
}