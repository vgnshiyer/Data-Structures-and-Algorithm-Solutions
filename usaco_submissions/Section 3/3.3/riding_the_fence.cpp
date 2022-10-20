#include <bits/stdc++.h>
using namespace std;

/*
TASK: fence
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long
#define nline "\n"

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

int F, n = -1;
vector<int> adj_list[501];

void remove_fence(int u, int v){
    for(int i = 0; i < adj_list[u].size(); i++)
        if(adj_list[u][i] == v){
            adj_list[u].erase(adj_list[u].begin() + i);
            break;
        }
    for(int i = 0; i < adj_list[v].size(); i++)
        if(adj_list[v][i] == u){
            adj_list[v].erase(adj_list[v].begin() + i);            
            break;
        }
}

void find_tour(int start, vector<int>& path){
    stack<int> stk;
    stk.push(start);
    while(!stk.empty()){
        int v = stk.top();
        int i;
        if(adj_list[v].size() == 0){
            path.push_back(v);
            stk.pop();
        } else {
            int next = adj_list[v][0];
            stk.push(next);
            // remove the edge from the graph so that it never gets traversed again
            remove_fence(v, next);
        }
    }
}

void refine(vector<int>& path, int v1, int v2){
    for(int i = 0; i < path.size()-1; i++){
        if((path[i] == v1 && path[i+1] == v2) || (path[i] == v2 && path[i+1] == v1)){
            vector<int> path2;
            for(int j = i+1; j < path.size(); j++)
                path2.push_back(path[j]);
            for(int j = 1; j <= i; j++)
                path2.push_back(path[j]);
            path = path2;
            break;
        }
    }
}

void solve(){
    cin >> F;
    for(int i = 0; i < F; i++){
        int u, v;
        cin >> u >> v;
        n = max({n,u,v});
        adj_list[u].push_back(v);
        adj_list[v].push_back(u);
    }

    for(int i = 1; i <= n; i++)
        sort(adj_list[i].begin(), adj_list[i].end());

    int v1 = -1, v2 = -1;
    for(int i = 1; i <= n; i++){
        if(adj_list[i].size() % 2){
            if(v1 == -1) v1 = i;
            else if(v2 == -1) v2 = i;
            else cerr << "invalid graph\nAborting...";
        }
    }
    if(v1 != -1){
        adj_list[v1].push_back(v2);
        adj_list[v2].push_back(v1);
    }

    vector<int> best_path;
    find_tour((v1 != -1 ? v1 : 1), best_path);
    if(v1 != -1) refine(best_path, v1, v2);
    for(auto it = best_path.rbegin(); it != best_path.rend(); it++)
        cout << *it << nline;
}

int main() {
    read_input("fence");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}