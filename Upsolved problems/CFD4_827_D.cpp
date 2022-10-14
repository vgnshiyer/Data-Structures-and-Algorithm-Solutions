/*
Given an array of n positive integers a1,a2,…,an (1≤ai≤1000). Find the maximum value of i+j such that ai and aj are coprime,† or −1 if no such i, j exist.

For example consider the array [1,3,5,2,4,7,7]. The maximum value of i+j that can be obtained is 5+7, since a5=4 and a7=7 are coprime.

Constraints: 
n ~ 10^5
a ~ 1000

Analysis: 
Realy contraints to the problem are not the value of n. It is actually the value of a with which we can solve the problem using a greedy approach.

since there are just 1000 numbers, we precalculate all the pairs of coprimes from it. 
Now we store the indices of the elements in the array and check whether any of its coprimes are present in the array or not. If such a coprime is present, we take the greatest indices of both i and j  and simultaneously update the answer.
*/

#include <bits/stdc++.h>
using namespace std;

bool testcases = 1;

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

void solve(){
    vector<int> coprimes[1001];
    vector<int> id(1001, -1);
    int n; 
    
    for(int i =1; i <= 1000; i++)
    for(int j =1; j <= 1000; j++)
        if(__gcd(i, j) == 1)
            coprimes[i].push_back(j);

    cin >> n;
    for(int i = 1; i <= n; i++){
        int x; cin >> x;
        id[x] = i;
    }

    int best = -1;
    for(int i = 1; i <= 1000; i++){
        if(id[i] == -1) continue; // element not present in the array
        for(int j : coprimes[i]){
            if(id[j] == -1) continue;
            best = max(best, id[i] + id[j]);
        }
    }
    cout << best << "\n";
}

int main() {
    fast_read();
    
    #ifndef ONLINE_JUDGE
    read_input("file");
    #endif

    ll tc = 1;
    if(testcases) cin>>tc;
    while(tc--)
        solve();
    return 0;
}