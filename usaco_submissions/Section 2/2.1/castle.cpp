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

vector<int> adj_list[2510];
bool visited[2510];

void add_edge(int x, int y){
    adj_list[x].push_back(y);
}

int N, M;

int get_destination(int s, int d){
    switch (d){
    case 0:
        return s-1;
    case 1:
        return s-M;
    case 2:
        return s+1;
    case 3:
        return s+M;
    default:
        break;
    }
}

void print_graph(int total){
    for(int i = 1; i <= total; i++){
        cout << i << "->";
        for(int k = 0; k < adj_list[i].size(); k++){
            cout << adj_list[i][k] << "->";
        }
        cout << "\n";
    }
}

int DFS(int x, int &count){
    visited[x] = true;
    count++;
    for(int next : adj_list[x])
        if(!visited[next])
            DFS(next, count);
}

void solve(){
    cin >> M >> N;
    int total = N*M;
    for(int node = 1; node <= total; node++){
        int x; cin >> x;
        for(int c = 0; c < 4; c++)
            if((x & (1 << c)) == 0)
                add_edge(node, get_destination(node, c));
    }

    // print_graph(total);
    
    // counting number of rooms
    // same as counting number of connected components in a graph
    int ans = 0, largest = -1;
    for(int i = 1; i <= total; i++){
        if(visited[i]) continue;
        int count = 0;
        DFS(i, count);
        largest = max(largest, count); // largest room in the palace
        ans++;
    }
    cout << ans << "\n";
    cout << largest << "\n";
}

int main() {
    read_input("file");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}