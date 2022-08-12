#include <bits/stdc++.h>
using namespace std;

/*
TASK: barn1
USER: Vignesh Iyer
LANG: C++
*/

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

void solve(){
    int m, s, c;
    cin >> m >> s >> c;
    vector<int> gaps;
    vector<int> barns;
    for(int i = 0; i < c; i++){
        int x; cin >> x;
        barns.push_back(x);
    }
    sort(barns.begin(), barns.end());

    for(int i = 1; i < c; i++) gaps.push_back(barns[i] - barns[i-1] - 1);

    sort(gaps.begin(), gaps.end(), greater<int>());
    int ans = 0, i = 0;

    ans += (barns[0] - 1); // length of gap between barn 1 and first barn with cows
    ans += s - barns[barns.size()-1]; // length of gap between barn S and last barn with cows
    while(m-- > 1 && i < c-1) ans += gaps[i++]; // length of gaps in middle
    
    cout << s - ans << "\n";
}

int main() {
    read_input("barn1");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}