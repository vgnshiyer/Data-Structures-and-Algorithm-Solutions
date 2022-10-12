#include <bits/stdc++.h>
using namespace std;

/*
TASK: kimbits
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long
#define nline "\n"

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

ll n, l, I;

/* Calculate binomial coefficient (n choose k) */
int dp[33][33];
int getSizeOfSet(int n, int k){
    if(n == 0 || k == 0) return 1;
    if(dp[n][k] != 0) return dp[n][k];

    return dp[n][k] = getSizeOfSet(n-1, k) + getSizeOfSet(n-1, k-1);
}

void solve(){
    cin >> n >> l >> I;
    
    for(int i = n; i > 0; i--){
        int s = getSizeOfSet(i-1, l);
        if(s < I){
            cout << 1;
            l--;
            I -= s;
        } else{
            cout << 0;
        }
    }
    cout << nline;
}   

int main() {
    read_input("kimbits");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}