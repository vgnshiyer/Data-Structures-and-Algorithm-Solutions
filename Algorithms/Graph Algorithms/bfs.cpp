#include <bits/stdc++.h>
using namespace std;

const int N = 1e5;
const int INF = 1e6;
vector<int> adj_list[N];
int dist[N];
int pred[N];

void add_edge(int x, int y){
    adj_list[x].push_back(y);
    adj_list[y].push_back(x);
}

void BFS(int source, int n){
    for(int i = 0; i < n; i++){
        dist[i] = -INF; // initially all nodes are not connected.
        pred[i] = -1;
    }
    dist[source] = 0;
    queue<int> q;
    q.push(source);
    while(!q.empty()){
        int curr = q.front();
        q.pop();

        for(int next_node : adj_list[curr]){
            if(dist[next_node] == -INF){
                dist[next_node] = dist[curr] + 1;
                q.push(next_node);
                pred[next_node] = curr;
            }
        }
    }
}

int main(){
    int n = 7;

    unordered_map<int, string> city;
    city[0] = "mumbai";
    city[1] = "thane";
    city[2] = "kurla";
    city[3] = "vashi";
    city[4] = "dombivili";
    city[5] = "ghansoli";
    city[6] = "ambernath";

    add_edge(0, 1);
	add_edge(0, 3);
	add_edge(1, 2);
	add_edge(1, 5);
	add_edge(1, 4);
	add_edge(3, 5);
	add_edge(4, 6);
	add_edge(5, 4);

    BFS(0, n);
    cout << "\nShortest Distance from mumbai to ambernath is: " << dist[6] <<0<< "kms.";
    vector<int> path;

    int crawl = 6;
    while(pred[crawl] != -1){
        path.push_back(pred[crawl]);
        crawl = pred[crawl];
    }
    cout << "\nThe shortest path is: ";
    for(int i = path.size()-1; i >=0; i--){
        cout << city[path[i]] << "->";
    }
    cout << city[6];
    // output
    //  Shortest Distance from mumbai to ambernath is: 30kms.
    //  The shortest path is: mumbai->thane->dombivili->ambernath 

    return 0;
}