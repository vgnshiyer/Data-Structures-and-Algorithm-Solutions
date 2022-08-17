#include <bits/stdc++.h>
using namespace std;

/*
TASK: frac1
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long
#define nline "\n"

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

int N;

bool compare(pair<int, int> a, pair<int, int> b){
    return (double)a.first/a.second < (double)b.first/b.second;
}

void solve(){
    cin >> N;
    vector<pair<int, int>> ans;
    unordered_set<double> fractions;

    for(int n = 0; n <= N; n++){
        for(int d = 1; d <= N; d++){
            double frac = (double)n/d;
            if(frac < 0 || frac > 1) continue;
            if(fractions.find(frac) == fractions.end()){
                ans.push_back(make_pair(n, d));
                fractions.insert(frac);
            }
        }
    }

    sort(ans.begin(), ans.end(), compare);
    for(int i = 0; i < ans.size(); i++)
        cout << ans[i].first << "/" << ans[i].second << "\n";
}

int main() {
    read_input("frac1");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}