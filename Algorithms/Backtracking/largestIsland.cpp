#include<bits/stdc++.h>
using namespace std;

int dx[8] = {0, 1, 0, -1, 1, 1, -1, -1};
int dy[8] = {1, 0, -1, 0, -1, 1, 1, -1};

void largestIsland(int& ans, vector<string>& map, int x, int y, int n, int m, int cnt){
    ans = max(ans, cnt);
    for(int i = 0; i < 8; i++){
        int xi = x + dx[i], yi = y + dy[i];

        if(xi < 0 || xi >= n || yi < 0 || yi >= m) continue;
        if(map[xi][yi] == '.' || map[xi][yi] != '1') continue;

        map[xi][yi] = '.';
        largestIsland(ans, map, xi, yi, n, m, cnt+1);
    }
}

int main(){
    vector<string> map = {"11000", "01100", "00101", "10001", "01011"};
    int ans = -1;

    int n = map.size(), m = map[0].size();
    for(int i = 0; i < n; i++)
    for(int j = 0; j < m; j++){
        if(map[i][j] =='1'){
            map[i][j] = '.';
            largestIsland(ans, map, i, j, n, m, 1);
        }
    }

    cout << "ans = " << ans << endl; 
    return 0;
}