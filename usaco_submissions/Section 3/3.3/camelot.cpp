#include <bits/stdc++.h>
using namespace std;

/*
TASK: camelot
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long
#define nline "\n"

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

struct pos{
    int x;
    int y;
};

int R, C;
pos king;
vector<pos> knights;
int cost[30][30][30][30];
const int INF = 1e6;

void bfs(vector<int> dx, vector<int> dy){
    int n = dx.size();

    for(int i = 0; i < R; i++)
    for(int j = 0; j < C; j++){
        /* init */
        for(int x = 0; x < R; x++)
        for(int y = 0; y < C; y++)
            cost[i][j][x][y] = INF;
        
        cost[i][j][i][j] = 0;
        queue<pos> q;
        pos p = {i,j};
        q.push(p);

        while(!q.empty()){
            auto curr = q.front();
            q.pop();

            for(int k = 0; k < n; k++){
                pos nxt = {curr.x + dx[k], curr.y + dy[k]};

                if(nxt.x < 0 || nxt.x >= R || nxt.y < 0 || nxt.y >= C) continue;
                if(cost[i][j][nxt.x][nxt.y] != INF) continue;

                if(cost[i][j][curr.x][curr.y] + 1 < cost[i][j][nxt.x][nxt.y])
                    cost[i][j][nxt.x][nxt.y] = cost[i][j][curr.x][curr.y] + 1;

                q.push(nxt);
            }
        }
    }
}

void solve(){
    /* Input routine */
    cin >> R >> C;
    
    char c; int x;
    cin >> c >> x;
    king.x = R - x;
    king.y = int(c - 'A');

    while(cin >> c >> x){
        pos knight;
        knight.x = R - x;
        knight.y = int(c - 'A');
        knights.push_back(knight);
    }

    /* Calculating path costs for knight */
    bfs({ 2, 2, -2, -2, 1, 1, -1, -1 }, { -1, 1, 1, -1, 2, -2, 2, -2 });
    
    /* Main routine */
    int best = INT_MAX;
    for(int i = 0; i < R; i++)
    for(int j = 0; j < C; j++){
        int s1 = 0;
        for(auto k : knights)
            s1 += cost[i][j][k.x][k.y];

        int mn = max(abs(king.x - i), abs(king.y - j));
        for(int x = king.x - 2; x <= king.x + 2; x++)
        for(int y = king.y - 2; y <= king.y + 2; y++){
            if(x < 0 || x >= R || y < 0 || y >= C) continue;
            for(auto z : knights){
                int s2 = cost[z.x][z.y][x][y] + max(abs(king.x - x), abs(king.y - y)) + cost[x][y][i][j] - cost[i][j][z.x][z.y];
                mn = min(mn, s2);
            }
        }
        best = min(best, s1 + mn);
    }

    cout << best << nline;
}

int main() {
    read_input("camelot");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}