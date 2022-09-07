#include <bits/stdc++.h>
using namespace std;

/*
TASK: ttwo
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long
#define nline "\n"

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

char farm[10][10];
int a, b, c, d;
int moves[4][2] = {{-1,0} ,{0,1}, {1,0}, {0,-1}};
bool memo[10][10][10][10][4][4];

bool valid_move(int p1, int p2,int dir){
    int x = p1+moves[dir][0], y = p2+moves[dir][1];
    if(x < 0 || x >= 10 || y < 0 || y >= 10) return false;
    if(farm[x][y] == '*') return false;
    return true;
}

int move(int &p1, int &p2, int dir){
    if(valid_move(p1, p2, dir)){
        p1 += moves[dir][0];
        p2 += moves[dir][1];
    }
    else
        dir = (dir + 1)%4;
    return dir;
}

void simulate(){
    // cow starts from a, b
    // farmer starts from c, d

    int d1 = 0, d2 = 0; // both start moving in the north dir initially
    for(int t = 0; ; t++){
        if(a == c && b == d){
            cout << t << nline;
            break;
        }
        if(memo[a][b][c][d][d1][d2]){
            cout << 0 << nline;
            break;
        }
        memo[a][b][c][d][d1][d2] = true;
        d1 = move(a,b,d1); // move cow
        d2 = move(c,d,d2); // move farmer
    }
}

void solve(){
    for(int i = 0; i < 10; i++)
    for(int j = 0; j < 10; j++){
        cin >> farm[i][j];
        if(farm[i][j] == 'C') a = i, b = j;
        else if(farm[i][j] == 'F') c = i, d = j;
    }

    simulate();
}

int main() {
    read_input("ttwo");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}