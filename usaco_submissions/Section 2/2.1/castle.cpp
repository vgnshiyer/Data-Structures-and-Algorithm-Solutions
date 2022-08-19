#include <bits/stdc++.h>
using namespace std;

/*
TASK: castle
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long
#define nline "\n"

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

struct room{
    int wall;
    int room_num;
};

int C[4] = {-1, 0, 1, 0};
int R[4] = {0, -1, 0, 1};
int walls[2] = {-1,-1};
int M, N;
int best = -1;
char dir;
vector<vector<room>> castle;

void update_len(int len, int r, int c, char w){
    if(len > best){ // if new len is greater, simple replace everything
        best = len;
        walls[0] = r, walls[1] = c;
        dir = w;
    }
    else if(len == best){
        if(c < walls[1]){ // priority to west (minimize c)
            walls[0] = r;
            walls[1] = c;
            dir = w;
        }
        else if(c == walls[1]) // tied? check south dir
            if(r > walls[0]){
                walls[0] = r;
                dir = w;
            }
        else if(c == walls[1] && r == walls[0]) // still tied? check north wall or east wall
            dir = w;
    }
}

void find_largest_room(unordered_map<int, int> room_len){
    for(int r = 0; r < N; r++)
    for(int c = 0; c < M; c++){
        // check if we can break the east wall and extend our current room?
        if(c < M-1 && castle[r][c].room_num != castle[r][c+1].room_num)
            update_len(room_len[castle[r][c].room_num] + room_len[castle[r][c+1].room_num], r, c, 'E');
        // check if we can break the north wall and extend our current room?
        if(r && castle[r][c].room_num != castle[r-1][c].room_num)
            update_len(room_len[castle[r][c].room_num] + room_len[castle[r-1][c].room_num], r, c, 'N');
    }
}

void DFS(int r, int c, int &len, int num){
    if(castle[r][c].room_num) return; // if module was visited earlier, skip it
    
    len++;
    castle[r][c].room_num = num; // assign room number to module

    for(int i = 0; i < 4; i++)
        if((castle[r][c].wall & (1 << i)) == 0)
            DFS(r+R[i], c + C[i], len, num); // explore the connected modules
}

void solve(){
    cin >> M >> N;
    castle.resize(N, vector<room>(M));
    unordered_map<int, int> room_len;

    for(int r = 0; r < N; r++)
    for(int c = 0; c < M; c++)
        cin >> castle[r][c].wall;

    // finding number of rooms is same as finding number of connected components in a graph
    int num_of_rooms = 0, num = 1, len, largest_room = -1;
    for(int r = 0; r < N; r++)
    for(int c = 0; c < M; c++){
        if(castle[r][c].room_num)continue; // if room was visited skip it
        num_of_rooms++; // count connected components when u enter a new room
        
        len = 0;
        DFS(r,c,len,num); // fully explore the new room and count its length
        room_len[num] = len;
        num++;
        largest_room = max(largest_room, len); // update biggest room length
    }

    cout << num_of_rooms << nline;
    cout << largest_room << nline;

    find_largest_room(room_len);
    cout << best << nline;
    cout << walls[0] + 1 << " " << walls[1] + 1 << " " << dir << nline;
}

int main() {
    read_input("castle");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}