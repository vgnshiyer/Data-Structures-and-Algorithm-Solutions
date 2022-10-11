#include <bits/stdc++.h>
using namespace std;

/*
TASK: msquare
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long
#define nline "\n"

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

unordered_set<string> visited;
string best;

void bfs(string start, string end){
    queue<pair<string, string>> q;
    q.push({"12345678", ""});

    while(!q.empty()){
        auto p = q.front();
        string curr = p.first;
        string path = p.second;
        q.pop();

        if(visited.count(curr)) continue;
        visited.insert(curr);

        if(curr == end){
            cout << path.length() << nline;
            cout << path << nline;
            return;
        }

        /* operation A */
        auto temp = string(curr.rbegin(), curr.rend());
        q.push({temp, path + 'A'});

        /* operation B */
        temp = string(1,curr[3]) + string(1,curr[0]) + string(1,curr[1]) + string(1,curr[2]) + string(1,curr[5]) + string(1,curr[6]) + string(1,curr[7]) + string(1,curr[4]);
        q.push({temp, path + 'B'});

        /* operation C */
        temp = string(1,curr[0]) + string(1,curr[6]) + string(1,curr[1]) + string(1,curr[3]) + string(1,curr[4]) + string(1,curr[2]) + string(1,curr[5]) + string(1,curr[7]);
        q.push({temp, path + 'C'});
    }
}

void solve(){
    string start, end;
    start = "12345678";

    for(int i = 0; i < 8; i++){
        char c; cin >> c;
        end += c;
    }

    bfs(start, end);
}   

int main() {
    read_input("msquare");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}