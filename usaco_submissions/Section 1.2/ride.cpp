#include <bits/stdc++.h>
using namespace std;

/*
TASK: ride
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

ll compute(string a){
    ll ans = 1;
    for(char x : a){
        ans *= (x-'A'+1);
        ans %= 47;
    }
    return ans;
}

void solve(){
    string a, b; cin >> a >> b;
    ll a_val = compute(a);
    ll b_val = compute(b);
    a_val == b_val ? cout << "GO\n" : cout << "STAY\n";
}

int main() {
    read_input("ride");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}