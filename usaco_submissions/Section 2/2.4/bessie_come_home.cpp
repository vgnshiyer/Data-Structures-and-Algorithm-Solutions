#include <bits/stdc++.h>
using namespace std;

/*
TASK: comehome
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long
#define nline "\n"
#define x first
#define y second
typedef pair<int, int> pi;

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

vector<pi> adj_list[100];
bool barns_with_cows[52];
int n;

void add_edge(int u, int v, int w){
    adj_list[u].push_back({v, w});
    adj_list[v].push_back({u, w});
}

struct compare{
    bool operator()(pair<int, int> a, pair<int, int> b){ return a.second > b.second; }
};

int Dijkstra(int u, int v){
    int dist[52];
    bool visited[52];
    for(int i = 0; i < 52; i++){
        dist[i] = (int)1e6;
        visited[i] = false;
    }

    dist[u] = 0;
    priority_queue<pair<int, int>, vector<pair<int, int>>, compare> pq;
    pq.push({u, 0});
    while(!pq.empty()){
        auto parent = pq.top();
        pq.pop();
        if(dist[parent.x] < parent.y) continue; // a smaller distance was already calculated
        for(auto child : adj_list[parent.x]){
            if(visited[child.x]) continue;
            if(dist[parent.x] + child.y < dist[child.x]){
                dist[child.x] = dist[parent.x] + child.y;
                pq.push({child.x,dist[child.x]});
            }
        }
        visited[parent.x] = true;
    }
    return dist[v];
}

void solve(){
    cin >> n;
    char src, dest;
    int w;
    for(int i = 0; i < n; i++){
        cin >> src >> dest >> w;
        int u = tolower(src) - 'a' + (isupper(src) ? 26 : 0);
        int v = tolower(dest) - 'a' + (isupper(dest) ? 26 : 0);
        add_edge(u, v, w);
        if(u > 25) barns_with_cows[u] = true;
        if(v > 25) barns_with_cows[v] = true;
    }
    barns_with_cows[51] = false;

    int best = INT_MAX, first_cow_barn = -1;
    for(int barn = 26; barn < 52; barn++){
        if(!barns_with_cows[barn]) continue;
        int d = Dijkstra(barn, 51);
        if(d < best){
            best = d;
            first_cow_barn = barn;
        }
    }
    cout << (char)(first_cow_barn - 26 + 'A') << " " << best << nline;
}

int main() {
    read_input("comehome");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}