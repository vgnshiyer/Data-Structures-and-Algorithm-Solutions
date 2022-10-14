/*
You are given a sequence a=[a1,a2,…,an] consisting of n positive integers.

Let's call a group of consecutive elements a segment. Each segment is characterized by two indices: the index of its left end and the index of its right end. Denote by a[l,r] a segment of the sequence a with the left end in l and the right end in r, i.e. a[l,r]=[al,al+1,…,ar].

For example, if a=[31,4,15,92,6,5], then a[2,5]=[4,15,92,6], a[5,5]=[6], a[1,6]=[31,4,15,92,6,5] are segments.

We split the given sequence a into segments so that:

each element is in exactly one segment;
the sums of elements for all segments are equal.

Analysis: 
We try all possible lengths in the array and recursively check the segments with sum with equal sums.
*/

#include <bits/stdc++.h>
using namespace std;

bool testcases = 1;
int n;
vector<int> arr;

int go(int i, int sum){
	if(i == n) return 0;
	int curr = 0;
	for(int j = i; j < n; j++){
		curr += arr[j];
		if(curr == sum) return max(j-i+1, go(j+1, sum));
		if(curr > sum) return n;
	}
	return n;
}

void solve(){
	cin >> n;
	arr.resize(n, 0);
	
	for(int &x : arr) cin >> x;
	
	int best = n, sum =0;
	for(int len = 1; len <= n; len++){
		sum += arr[len-1];
		best = min(best, go(0, sum));
	}
	cout << best << nline;
}

int main() {
    fast_read();
    
    //#ifndef ONLINE_JUDGE
    freopen("beads.in", "r", stdin);
    freopen("beads.out", "w", stdout);
    //#endif

    int tc=1; 
    if(testcases) cin>>tc;
    while(tc--)
        solve();
        
    return 0;
}