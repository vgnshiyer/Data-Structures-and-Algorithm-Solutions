#include <bits/stdc++.h>
using namespace std;

/*
TASK: hamming
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long
#define nline "\n"

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

int n, b, d;

int hamming_distance(int x, int y){
    x ^= y;
    int diff = 0;
    while(x){
        diff += x & 1;
        x >>= 1;
    }
    return diff;
}

bool valid(vector<int> ans, int mask){
    for(int i = 0; i < ans.size(); i++)
        if(hamming_distance(ans[i], mask) < d) return false;
    return true;
}

void solve(){
    cin >> n >> b >> d;
    vector<int> ans = {0};
    for(int mask = 0; ans.size() < n && mask < (1 << b); mask++){
        if(valid(ans, mask))
            ans.push_back(mask);
    }
    // sort(ans.begin(), ans.end());

    for(int i = 0; i < ans.size(); i++) cout << ans[i] << " \n"[i%10 == 9 || i == n-1];
}

int main() {
    read_input("hamming");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}