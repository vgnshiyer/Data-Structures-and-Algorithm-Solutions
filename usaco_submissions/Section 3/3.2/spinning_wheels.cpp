#include <bits/stdc++.h>
using namespace std;

/*
TASK: spin
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long
#define nline "\n"

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

int speed[5];
vector<pair<int, int>> wedge[5];
int path[360];
int n;

bool inital_position(vector<int> init){
    int sum = 0; 
    for(int x : init) sum += x;
    return sum == 0;
}

bool light_passes() {
    for(int i = 0; i < 360; i++)
        if(path[i] == 5) return true;
    return false;
}

void solve(){
    for(int i = 0; i < 5; i++){
        cin >> speed[i];
        cin >> n;
        for(int j = 0 ; j < n; j++){
            int x, y;
            cin >> x >> y;
            wedge[i].push_back({x,y});
        }
    }

    vector<int> init = {0,0,0,0,0};
    int t = 0;
    while(true){
        fill(path, path+360, 0);
        for(int i = 0; i < 5; i++)
        for(auto p : wedge[i])
        for(int j = p.first; j <= p.first+p.second; j++){
            path[j % 360]++;
        }
        
        if(light_passes()){
            cout << t << nline;
            return;
        }

        // simulate the wedges
        for(int i = 0; i < 5; i++)
        for(auto &p : wedge[i]){
            p.first += speed[i];
            p.first %= 360;
        }

        // simulate the wheels
        for(int i = 0; i < 5; i++)
            init[i] = (init[i] + speed[i])%360;
        
        if(inital_position(init))
            break;
        t++;
    }
    cout << "none\n";
}

int main() {
    read_input("spin");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}