#include <bits/stdc++.h>
using namespace std;

/*
TASK: milk3
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long
#define nline "\n"

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

int A, B, C;
set<int> ans;
int visited[21][21][21];

void compute(int a, int b, int c){
    if(a == 0)
        ans.insert(c);

    if(!visited[a][b][c]){
        visited[a][b][c] = 1;

        int bucket[] = {a,b,c};
        int capacity[] = {A,B,C};
        for(int i = 0; i < 3; i++){
            for(int j = 0; j < 3; j++){
                if(i != j){
                    int need = min(bucket[i], capacity[j] - bucket[j]);
                    bucket[i] -= need, bucket[j] += need;
                    compute(bucket[0], bucket[1], bucket[2]);
                    bucket[i] += need, bucket[j] -= need; // backtrack
                }
            }
        }
    }
}

void solve(){
    cin >> A >> B >> C;
    compute(0, 0, C);
    
    vector<int> result(ans.begin(), ans.end());
    int n = result.size()-1;
    for(int i = 0; i <= n; i++)
        cout << result[i] << " \n"[i == n];
}

int main() {
    read_input("milk3");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}