#include <bits/stdc++.h>
using namespace std;

/*
TASK: lamps
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long
#define nline "\n"

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

int N, C;
vector<int> ON, OFF;
set<string> ans;

bitset<101> simulate(bitset<101> bs, int button){
    switch (button){
    case 1:
        bs.flip();
        break;
    
    case 2:
        for(int i = 0; i < N; i += 2)
            bs.flip(i);
        break;

    case 3:
        for(int i = 1; i < N; i += 2)
            bs.flip(i);
        break;
    
    case 4:
        for(int i = 0; i < N; i += 3)
            bs.flip(i);
        break;
    
    default:
        break;
    }
    return bs;
}

bool check(bitset<101> bs){
    for(auto x : ON)
        if(bs[x-1] == 0) return false;

    for(auto x : OFF)
        if(bs[x-1] == 1) return false;
    return true;
}

void dfs(bitset<101> bs, int c){
    if(c == C){
        if(check(bs)){
            auto bin = bs.to_string();
            bin = bin.substr(bin.size() - N);
            reverse(bin.begin(), bin.end());
            ans.insert(bin);
        }
        return;
    }

    for(int i = 1; i <= 4; i++)
        dfs(simulate(bs, i), c+1);
}

void solve(){
    cin >> N >> C;
    C = C > 3 ? 4 : C; // only the first 2^4 flips matter
    bitset<101> bs;
    bs.set(); // all lights are on by default in the beginning
    int x;
    while(cin >> x){
        if(x == -1) break;
        ON.push_back(x);
    }
    while(cin >> x){
        if(x == -1) break;
        OFF.push_back(x);
    }
    
    dfs(bs, 0); // try all possible combinations of button flips
    if(ans.size() == 0) cout << "IMPOSSIBLE" << nline;
    else
        for(auto x : ans) cout << x << nline;
}

int main() {
    read_input("lamps");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}