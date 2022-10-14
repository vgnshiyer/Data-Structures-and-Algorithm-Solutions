/*
Given two positive integers N and M,let S denote the set of all arrays of length N with elements which lie in the range [1, M]. 

Let Xi denote the bitwise AND of the elements in the ith Array of the set S.
Find the sum of all X for all M^N arrays.

Analysis: 
Since the constraints for M are very big(10^9), we need to solve it in a different way. 

We can iterate over the bits, instead of the actual numbers.
Consider below example:
3 + 2 = (11)2 + (10)2 = n(1)2*2 + n(1)1*1 = 3

Therefore, all we need to find is, the contribution of the ith bit over all its permutations to the total sum.

First we will find the count of numbers in the range[1,M] which have the ith bit set. 
lets call this ct(i). Now we do ct(i)^N permutations. 
Finally we multiply it with the power of 2(1 << i) and add it to the total sum.

*/

#include <bits/stdc++.h>
using namespace std;

const ll MOD = 998244353;
bool testcases = 1;

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

ll binpow(ll a, ll b){
    ll ans=1;
    
    while(b>0){
        if((b%2)==1){
            ans=(ans*a)%MOD;
        }
        b/=2;
        a=(a*a)%MOD;
    }
    return ans;
}

ll getCount(ll m, ll i){
    ll ans = ((m >> (i+1)) << i);
    if((m >> i) & 1) 
        ans += (m & ((1 << i) - 1));
    return ans;
}

void solve(){
    ll n, m;
    cin >> n >> m;

    ll ans = 0;
    for(int i = 0; i <= 32; i++){
        if((1 << i) > m) break;
        ll p = getCount(m+1, i);
        p = binpow(p, n);
        ans=(ans+((p*(1 << i))%MOD))%MOD;
    }
    cout << ans << nline;
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