#include <bits/stdc++.h>
using namespace std;

/*
TASK: maze1
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long
#define nline "\n"
#define F first
#define S second
typedef pair<int, int> pii;

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

int w, h;
vector<string> maze;
vector<pii> exits;

int deltax[4] = {-1, 1, 0, 0}, deltay[4] = {0, 0, -1, 1};

void get_exits(){
    // search first row
    for(int i = 0; i < w; i++) 
        if(maze[0][i] == ' ')
            exits.push_back({1, i});

    // search last column
    for(int i = 0; i < h; i++)
        if(maze[i][w-1] == ' ')
            exits.push_back({i, w-2});
            
    // search last row
    for(int i = 0; i < w; i++)
        if(maze[h-1][i] == ' ')
            exits.push_back({h-2, i});

    // search first column
    for(int i = 0; i < h; i++)
        if(maze[i][0] == ' ')
            exits.push_back({i, 1});
}


void DFS(pii cell, int cnt, vector<vector<int>> &dist){
    if(cell.F < 0 || cell.F >= h || cell.S < 0 || cell.S >= w) return;
    if(cnt >= dist[cell.F][cell.S]) return;

    dist[cell.F][cell.S] = cnt;

    for(int i = 0; i < 4; i++){
        int xx = cell.F + deltax[i], yy = cell.S + deltay[i];
        if(maze[xx][yy] == ' ')
            DFS({xx + deltax[i], yy + deltay[i]}, cnt + 1, dist);
    }
}

void solve(){
    cin >> w >> h;
    w = w*2 + 1, h = h*2 + 1;
    string line;
    while(getline(cin, line))
        maze.push_back(line);
    maze.erase(maze.begin());

    get_exits(); // get the exit points in the labyrinth

    vector<vector<int>> dist(h+1, vector<int>(w+1, 1e6));
    for(auto exit : exits)
        DFS(exit, 1, dist);

    int best = -1;
    for(int i = 0; i < h; i++)
    for(int j = 0; j < w; j++){
        if(dist[i][j] == 1e6) continue;
        best = max(best, dist[i][j]);
        // if(dist[i][j] != -1) cout << dist[i][j] << " \n"[j == w-2];
    }
    cout << best << nline;
}

int main() {
    read_input("maze1");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}