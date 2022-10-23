#include <bits/stdc++.h>
using namespace std;

vector<int> seg;

void buildTree(vector<int> arr, int n){
    for(int i = 0; i < n; i++) seg[n+i] = arr[i];

    for(int i = n-1; i >= 1; i--)
        seg[i] = seg[2*i] + seg[2*i+1];
}

int query(int idx, int l, int r, int ql, int qr){
    if(ql > r || qr < l) return 0;
    if(l >= ql && r <= qr) return seg[idx];

    int mid = (l + r) >> 1;
    return query(2*idx, l, mid, ql, qr) + query(2*idx+1, mid+1, r, ql, qr);
}

void update(int i, int v, int n){
    seg[n+i] = v;
    for(int j = (n+i)/2; j >= 1; j /= 2){
        seg[j] = seg[2*j] + seg[2*j+1];
    }
}

int main(){
    int n = 6;
    vector<int> arr = {1, 2, 6, 7, 4, 3};

    while(__builtin_popcount(n) != 1){
        n++;
        arr.push_back(0);
    }

    seg.resize(2*n, 0);

    buildTree(arr, n);

    // for(int x : seg) cout << x << " ";
    // cout << "\n";

    cout << query(1, 0, n-1, 0, 2) << "\n";
    update(2, 8, n); // update element at pos 2 to 8
    cout << query(1, 0, n-1, 0, 2) << "\n";
}