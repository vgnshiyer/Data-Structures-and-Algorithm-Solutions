#include <bits/stdc++.h>
using namespace std;

/*
Eulerian Cycle: An undirected graph has Eulerian cycle if following two conditions are true. 

* All vertices with non-zero degree are connected. We don’t care about vertices with zero degree because they don’t belong to Eulerian Cycle or Path (we only consider all edges). 
* All vertices have even degree.

Eulerian Path: An undirected graph has Eulerian Path if following two conditions are true. 

* Same as condition (a) for Eulerian Cycle.
* If zero or two vertices have odd degree and all other vertices have even degree. Note that only one vertex with odd degree is not possible in an undirected graph (sum of all degrees is always even in an undirected graph)

We will see three graphs.   
                                          +---------+
                                          |         |
  1----0----3          1----0----3        1----0----3
  |  /      |          |  /   \  |        |  /      |
  | /       |          | /     \ |        | /       |
  2         4          2         4        2         4 

To find the Eulerian path / Eulerian cycle we can use the following strategy: We find all simple cycles and combine them into one - this will be the Eulerian cycle. If the graph is such that the Eulerian path is not a cycle, then add the missing edge, find the Eulerian cycle, then remove the extra edge.
*/

const int N = 1000;
vector<int> adj_list[N]; 

void add_edge(int u, int v){
    adj_list[u].push_back(v); 
    adj_list[v].push_back(u);
}

int isEulerian(int n){
    int odd_nodes = 0;
    for(int i = 0; i < n; i++)
        if(adj_list[i].size() % 2) odd_nodes++;

    if(odd_nodes && odd_nodes == 2){
        return 0;
        // cout << "The Graph has an Eulerian path but no circuit\n";
    } else if(odd_nodes == 0) {
        return 1;
        // cout << "The Graph has both Eulerian Path and Circuit\n";
    } else{
        return 2;
        // cout << "The Graph is not Eulerian\n";
    }
}

void delete_edge(int u, int v){
    for(int i = 0; i < adj_list[u].size(); i++){
        if(adj_list[u][i] == v){
            adj_list[u].erase(adj_list[u].begin() + i);
            break;
        }
    }

    for(int i = 0; i < adj_list[v].size(); i++){
        if(adj_list[v][i] == u){
            adj_list[v].erase(adj_list[v].begin() + i);
            break;
        }
    }
}

vector<int> getEulerianPath(int n){
    // if(isEulerian(n) == 2) {
    //     cout << "Graph does not contain either a Eulerian path or a cycle\n";
    //     return {};
    // }

    int v1 = -1, v2 = -1;
    if(isEulerian(n) == 0){
        for(int i = 0; i < n; i++){
            if(adj_list[i].size() % 2){
                if(v1 == -1) v1 = i;
                else if(v2 == -1) v2 = i;
                else cerr << "Not a valid graph\n";
            }
        }
        add_edge(v1,v2); // make a eulerian cycle.
    }

    int start = (v1 != -1 ? v1 : 0);
    // The Algorithm
    stack<int> stk;
    stk.push(start);
    vector<int> res;
    while(!stk.empty()){
        int v = stk.top();
        int i;
        if(adj_list[v].size() == 0){
            res.push_back(v);
            stk.pop();
        } else {
            int next = adj_list[v][0];
            stk.push(next);
            // remove the edge from the graph so that it never gets traversed again
            delete_edge(v, next);
        }
    }

    if(v1 != -1){
        for(int i = 0; i < res.size()-1; i++){
            if((res[i] == v1 && res[i+1] == v2) || (res[i] == v2 && res[i+1] == v1)){
                vector<int> res2;
                for(int j = i+1; j < res.size(); j++)
                    res2.push_back(res[j]);
                for(int j = 1; j <= i; j++)
                    res2.push_back(res[j]);
                res = res2;
                break;
            }
        }
    }

    return res;
}

int main(){
    int n = 5;
    /*graph 1
    Has Eulerian Path but no circuit*/
    add_edge(1,0);
    add_edge(0,2);
    add_edge(2,1);
    add_edge(0,3);
    add_edge(3,4);
    // add_edge(0,4); // second graph
    add_edge(1,3); // third graph

    for(int x : getEulerianPath(n)) cout << x << " ";
    /*
    graph 1 : 4 3 0 2 1 0
    graph 2 : 0 4 3 0 2 1 0
    graph 3 : Graph does not contain either path or cycle
    */
}