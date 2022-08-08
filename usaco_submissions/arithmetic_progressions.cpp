#include <bits/stdc++.h>
using namespace std;

/*
TASK: ariprog
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long
#define nline "\n"
#define sq(x) (x)*(x)

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

int N, M;
int bs[2*251*251];
set<int> bisquares;

void generate_bisquares(int M){
    for(int p = 0; p <= M; p++){
        for(int q = p; q <= M; q++){
            int val = sq(p)+sq(q);
            bs[val] = 1;
            bisquares.insert(val);
        }
    }
}

bool check(int a, int d){
    for(int i = 0; i < N; i++){
        if(!bs[a + i*d]) return false;
    }
    return true;
}

void solve(){
    cin >> N >> M;
    generate_bisquares(M);

    vector<pair<int, int>> ans;
    for(auto num : bisquares){
        for(int d = 1; d <= (2*sq(M)-num)/(N-1); d++){ // a + (n-1)*d <= 2*sq(m)
            if(check(num, d)){
                ans.push_back(make_pair(d, num));
            }
        }
    }

    if(ans.size() == 0){
        cout << "NONE" << nline;
        return;
    }

    sort(ans.begin(), ans.end());
    for(int i = 0; i < ans.size(); i++)
        cout << ans[i].second << " " << ans[i].first << nline;
}

int main() {
    read_input("ariprog");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}