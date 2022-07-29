#include <bits/stdc++.h>
using namespace std;

/*
TASK: milk
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

void solve(){
    ll n, m; cin >> n >> m;
    vector<pair<ll, ll>> cost(m);
    for(ll i = 0; i < m; i++) cin >> cost[i].first >> cost[i].second;

    sort(cost.begin(), cost.end());
    ll units_left = n, c = 0;
    for(ll i = 0; i < m && units_left > 0; i++){
        if(cost[i].second <= units_left){
            units_left -= cost[i].second;
            c += (cost[i].first*cost[i].second);
        } else{
            c += (cost[i].first*units_left);
            units_left = 0;
        }
    }
    cout << c << "\n";
}

int main() {
    read_input("milk");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}