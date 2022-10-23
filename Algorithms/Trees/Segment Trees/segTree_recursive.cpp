#include <bits/stdc++.h>
using namespace std;

vector<int> seg;

void buildTree(vector<int> arr, int idx, int l, int r){
    if(l == r){
        seg[idx] = arr[l];
        return;
    }

    int mid = (l + r) >> 1;
    buildTree(arr, 2*idx, l, mid);
    buildTree(arr, 2*idx+1, mid+1, r);
    seg[idx] = seg[2*idx] + seg[2*idx+1];
}

int query(int idx, int l, int r, int ql, int qr){
    if(ql > r || qr < l) return 0;
    if(l >= ql && r <= qr) return seg[idx];

    int mid = (l + r) >> 1;
    return query(2*idx, l, mid, ql, qr) + query(2*idx+1, mid+1, r, ql, qr);
}

void update(int idx, int l, int r, int i, int v){
    if(i > r || i < l) return;
    if(l == r){
        seg[idx] = v;
        return;
    }

    int mid = (l + r) >> 1;
    update(2*idx, l, mid, i, v);
    update(2*idx+1, mid+1, r, i, v);
    seg[idx] = seg[2*idx] + seg[2*idx + 1];
}

int main(){
    int n = 6;
    vector<int> arr = {1, 2, 6, 7, 4, 3};

    while(__builtin_popcount(n) != 1){
        n++;
        arr.push_back(0);
    }

    seg.resize(2*n, 0);

    buildTree(arr, 1, 0, n-1);

    // for(int x : seg) cout << x << " ";
    // cout << "\n";

    cout << query(1, 0, n-1, 0, 2) << "\n";
    update(1, 0, n-1, 2, 8); // update element at pos 2 to 8
    cout << query(1, 0, n-1, 0, 2) << "\n";
}