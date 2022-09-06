/*
Minimum number of moves taken by a knight on a 8x8 chess board from position(x,y) to targetposition(tx,ty).
*/
#include <bits/stdc++.h>
using namespace std;

int getMinStepsToReachTarget(int x, int y, int tx, int ty){
    queue<pair<int, int>> q;
    q.push({x, y});

    vector<vector<bool>> visited(8,vector<bool>(8, false));
    vector<vector<int>> dist(8, vector<int>(8, -1));
    dist[x][y] = 0;
    
    while(!q.empty()){
        auto p = q.front();
        q.pop();

        int xx = p.first;
        int yy = p.second;

        if(xx == tx && yy == ty) return dist[xx][yy];

        if(visited[xx][yy]) continue;
        visited[xx][yy] = true;

        int ax[8] = { 2, 2, -2, -2, 1, 1, -1, -1 };
        int ay[8] = { -1, 1, 1, -1, 2, -2, 2, -2 };
        for(int i = 0; i < 8; i++){
            int nx = xx + ax[i];
            int ny = yy + ay[i];

            bool isValid = nx >= 0 && nx < 8 && ny >= 0 && ny < 8;
            if(isValid) {
                q.push({nx, ny});
                dist[nx][ny] = dist[xx][yy] + 1;
            }
        }
    }
}

int main(){
    int x = 7, y = 7;
    int tx = 7, ty = 5;

    cout << getMinStepsToReachTarget(x, y, tx, ty) << endl; // 2 moves
    return 0;
}