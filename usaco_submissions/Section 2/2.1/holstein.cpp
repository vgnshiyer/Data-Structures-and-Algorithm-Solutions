#include <bits/stdc++.h>
using namespace std;

/*
TASK: holstein
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long
#define nline "\n"

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

const int VMAX = 30;
const int GMAX = 20;

int V, G;

int reqd[VMAX];
int feed[GMAX][VMAX];

void solve(){
    cin >> V;
    for(int i = 0; i < V; i++) cin >> reqd[i];
    cin >> G;
    for(int i = 0; i < G; i++)
    for(int j = 0; j < V; j++)
        cin >> feed[i][j];

    int best = INT_MAX, feeds;
    for(int mask = 0; mask < (1 << G); mask++){ // mask goes from 0(including no feed) to 2^G-1(including all feeds)
        int sum[V] = {0};
        for(int i = 0; i < G; i++){
            if(mask & (1 << i)){ // if ith bit is set, 
                // include the ith feed.
                for(int j = 0; j < V; j++)
                    sum[j] += feed[i][j];
            }
        }
        bool found = true;
        for(int j = 0; j < V; j++)
            if(sum[j] < reqd[j]){
                found = false;
                break;
            }
        if(found){
            int curr = __builtin_popcount(mask);
            if(curr < best){
                best = curr;
                feeds = mask;
            }
        }
    }

    cout << best;
    for(int i = 0; i < G; i++)
        if(feeds & (1 << i)) cout << " " << i+1;
    cout << nline;
}

int main() {
    read_input("holstein");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}