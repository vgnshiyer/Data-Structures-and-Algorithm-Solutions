#include <bits/stdc++.h>
using namespace std;

/*
TASK: prefix
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long
#define nline "\n"

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

vector<string> P;
int dp[200005]; // dp at index i tells whether a prefix can be formed from index 0 to i-1 or not. 

void solve(){
    string x;
    while(cin >> x){
        if(x == ".") break;
        P.push_back(x);
    }

    string S;
    while(cin >> x) S += x;
    
    int n = (int)S.length();
    dp[0] = 1;
    int best = 0;
    for(int i = 0; i < n; i++){
        if(dp[i])
            for(auto p : P){
                string prefix = S.substr(i, p.length());
                if(prefix == p){
                    dp[i + p.length()] = true;
                    best = max(best, i+(int)p.length());
                }
            }
    }
    cout << best << nline;
}

int main() {
    read_input("prefix");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}