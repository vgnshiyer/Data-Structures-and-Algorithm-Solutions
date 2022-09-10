#include <bits/stdc++.h>
using namespace std;

/*
TASK: fracdec
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long
#define nline "\n"
#define F first
#define S second
typedef pair<int, int> pii;

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

int N, D;

void solve(){
    cin >> N >> D;
    if(N%D == 0) cout << N/D << ".0" << nline;
    else{
        cout << N/D << ".";
        int char_count = 2;
        char_count += to_string(N/D).length();
        unordered_map<int, int> hm;
        vector<int> order;
        unordered_set<int> seen;
        N %= D;
        int end = -1;
        while(true){
            N *= 10;
            if(seen.count(N)){
                end = N;
                break;
            }
            seen.insert(N);
            hm[N] = N/D;
            order.push_back(N);
            if(N%D == 0){
                for(int n : order){
                    if(char_count%76 == 1) cout << nline;
                    cout << hm[n];
                    char_count++;
                }
                cout << nline;
                return;
            }
            N %= D;
        }
        for(int n : order){
            if(char_count%76 == 1) cout << nline;
            if(n == end){
                cout << "(";
                char_count++;
            }
            cout << hm[n];
            char_count++;
        }
        cout << ")\n";
    }
}

int main() {
    read_input("fracdec");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}