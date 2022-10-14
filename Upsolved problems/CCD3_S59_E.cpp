/*
You are given a binary string S.

In one second, the following scenario happens simultaneously and independently for all the bits which are set to 1 in the string:

Change the bit from 1 to 0.
If the left neighbour exists and is 0, change it to 1.
If the right neighbour exists and is 0, change it to 1.
For example, if S = 010 S=010 initially, then after 1 second, S = 101 S=101 (the 1 bit and both its neighbours were changed). After another second, S = 010 S=010. Here, the first and the last bit were changed to 0 because earlier they were 1. The middle bit was changed because it was 0 earlier and it was a neighbour of a 1 bit.

Find out the string S after K seconds.

Analysis: 
Since K is a really big number, we cannot perform all the operations. 
However, notice something. Once any 0 participates in an operation, it is guaranteed that it will participate in the rest of the iterations.
eg. 001 -> 010 -> 101 -> 010 ....

Therefore, the problem really boils down to finding the first second a 0 becomes 1.
This is same as saying, we need to find the nearest 1 to a 0 either on the left or on the right side of the element.
*/

#include <bits/stdc++.h>
using namespace std;

const ll MOD = 998244353;
bool testcases = 1;

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

void solve(){
    ll n, k;
    cin >> n >> k;
    string s; cin >> s;

    vector<ll> dist(n, 10000000000);

    // finding min distance for 0 for nearest 1
    ll j = -1;
    for(ll i = 0; i < n; i++){
        if(s[i] == '1') j = i;
        else
            if(j != -1) dist[i] = i - j;
    }

    j = -1;
    for(ll i = n-1; i >= 0; i--){
        if(s[i] == '1') j = i;
        else
            if(j != -1) dist[i] = min(dist[i], j-i);
    }

    j = -1;
    // finding min distance for 1 with nearest 0
    for(ll i = 0; i < n; i++){
        if(s[i] == '0') j = i;
        else
            if(j != -1) dist[i] = i-j;
    }

    j = -1;
    for(ll i = n-1; i >= 0; i--){
        if(s[i] == '0') j = i;
        else 
            if(j != -1) dist[i] = min(dist[i], j-i);
    }

    for(ll i = 0; i < n; i++){
        if(s[i] == '0'){
            ll d = dist[i];
            if(d <= k)
                if((k - d + 1)%2) s[i] = '1';
                
        } else {
            s[i] = '0';
            ll d = dist[i];
            if(d <= k-1)
                if((k - d)%2) s[i] = '1';
        }
    }
    cout << s << nline;
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