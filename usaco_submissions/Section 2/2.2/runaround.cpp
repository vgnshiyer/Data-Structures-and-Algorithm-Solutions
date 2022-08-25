#include <bits/stdc++.h>
using namespace std;

/*
TASK: runround
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long
#define nline "\n"

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

ll m;

bool duplicates(string s){
    int n = s.length();
    unordered_set<char> seen;
    bool has_duplicates = false;
    for(char c : s){
        if(c == '0' || seen.count(c)) has_duplicates = true;
        seen.insert(c);
    }
    return has_duplicates;
}

bool is_runaround(ll num){
    string s = to_string(num);
    if(duplicates(s)) return false;

    int n = s.length();

    stack<pair<int, int>> stk;
    int start = int(s[0] - '0'); // the number where we start our search
    stk.push(make_pair(start, 0)); // stack stores the actual digit and the position of that digits
    bool visited[n] = {0}; // visited array stores if the digit was visited before or not

    int stop = 0;
    while(!stk.empty()){
        auto p = stk.top();
        stk.pop();
        if(visited[p.second]){ // if the digit was visited earlier, break out of the loop
            stop = p.first; // store the last seen element
            break; // continue would also work as the stack becomes empty and the loop will stop anyways
        }
        
        visited[p.second] = true; // mark the element as visited and proceed
        int end = p.first;
        int idx = p.second;
        idx = (idx+end)%n;
        stk.push(make_pair(int(s[idx] - '0'),idx)); // push the element
    }

    if(start != stop) return false; // if we dont arrive back to starting element after exploring all the other elements, return false

    for(int i = 0; i < n; i++) if(!visited[i]) return false; // if the number has any unvisited digit, return false
    return true;
}

void solve(){
    cin >> m;
    for(ll num = m+1; num <= 2e10; num++)
        if(is_runaround(num)){
            cout << num << nline;
            break;
        }
}

int main() {
    read_input("runround");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}