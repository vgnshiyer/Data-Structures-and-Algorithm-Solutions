#include <bits/stdc++.h>
using namespace std;

/*
TASK: skidesign
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

int N;
ll cost = 1e10;
int hills[1000];

void solve(){
    cin >> N;
    for(int i = 0; i < N; i++) cin >> hills[i];

    for(int i = 0; i <= 83; i++){
        int mx = i + 17;
        int temp_cost = 0;
        for(int j = 0; j < N; j++){
            if(hills[j] < i) temp_cost += sq(i - hills[j]);
            if(hills[j] > mx) temp_cost += sq(hills[j] - mx);
        }
        cost = min(cost, (ll)temp_cost);
    }
    cout << cost << nline;
}

int main() {
    read_input("skidesign");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}