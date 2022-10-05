#include <bits/stdc++.h>
using namespace std;

/*
TASK: ratios
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long
#define nline "\n"

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

int g[3];
int r[3][3];

void solve(){
    cin >> g[0] >> g[1] >> g[2];
    for(int i = 0; i < 3; i++)
    for(int j = 0; j < 3; j++) cin >> r[i][j];

    int sum = INT_MAX;
    int ans[4];

    for(int x = 0; x <= 100; x++)
    for(int y = 0; y <= 100; y++){
        if(x + y > sum) break;

        for(int z = 0; z <= 100; z++){
            if(x + y + z >= sum) break;

            int a = x*r[0][0] + y*r[1][0] + z*r[2][0];
            int b = x*r[0][1] + y*r[1][1] + z*r[2][1];
            int c = x*r[0][2] + y*r[1][2] + z*r[2][2];

            if((a+b+c)%(g[0]+g[1]+g[2])) continue;
            int d = (a+b+c)/(g[0]+g[1]+g[2]);

            int d1, d2, d3;
            if((g[0] == 0 && a != 0) || (a == 0 && g[0] != 0) || g[0]*d != a) continue;

            if((g[1] == 0 && b != 0) || (b == 0 && g[1] != 0)  || g[1]*d != b) continue;

            if((g[2] == 0 && c != 0) || (c == 0 && g[2] != 0)  || g[2]*d != c) continue;

            if(a+b+c < sum){
                // found a better answer;
                sum = a+b+c;
                ans[0] = x, ans[1] = y, ans[2] = z;
                ans[3] = d;
            }
        }
    }

    if(sum == INT_MAX) cout << "NONE\n";
    else
        for(int i = 0; i < 4; i++) cout << ans[i] << " \n"[i==3];
}   

int main() {
    read_input("ratios");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}