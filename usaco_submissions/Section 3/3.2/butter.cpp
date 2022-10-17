#include <bits/stdc++.h>
using namespace std;

/*
TASK: butter
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long
#define nline "\n"

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

int N, P, C;
vector<pair<int, int>> farm[801];
const int INF = 1e5;

struct compare{
    bool operator()(pair<int, int> a, pair<int, int> b){
        return a.first > b.first;
    }
};

void solve(){
    cin >> N >> P >> C;
    int cows[N];
    for(int i = 0; i < N; i++) cin >> cows[i];

    for(int i = 0; i < C; i++){
        int x, y, w;
        cin >> x >> y >> w;
        farm[x].push_back({w, y});
        farm[y].push_back({w, x});
    }

    int mn = INT_MAX;
    
    for(int i = 1; i <= P; i++){
        // try placing a sugar cube here
        // DIJKSTRA's
        vector<int> dist(P+1, INF);
        priority_queue<pair<int, int>, vector<pair<int, int>>, compare> pq;
        vector<bool> visited(P+1, false);
        dist[i] = 0;

        pq.push({0, i});
        while(!pq.empty()){
            auto p = pq.top();
            pq.pop();
            int node = p.second;
            int w = p.first;
            if(dist[node] < w) continue;

            for(auto n : farm[node]){
                if(visited[n.second]) continue;
                if(dist[node] + n.first < dist[n.second]){
                    dist[n.second] = dist[node] + n.first;
                    pq.push({dist[n.second], n.second});
                }
            }
            visited[node] = true;
        }
        int cost = 0;
        for(int c : cows) cost += dist[c];
            
        mn = min(mn, cost);
    }
    cout << mn << nline;
}

int main() {
    read_input("butter");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}