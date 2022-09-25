#include <bits/stdc++.h>
using namespace std;

/*
TASK: contact
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long
#define nline "\n"

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

int A, B, N;
string s;

void solve(){
    cin >> A >> B >> N;
    string temp;
    while(getline(cin, temp)) s+= temp;
    
    int n = s.length();
    unordered_map<string, int> hm;
    vector<string> freq[n+1];

    for(int i = A; i <= B; i++){
        if(i > n) break;
        for(int j = 0; j <= n-i; j++){
            hm[s.substr(j, i)]++;
        }
    }

    for(auto p : hm){
        if(!hm[p.first]) continue;
        freq[p.second].push_back(p.first);
    }

    for(int i = n; i > 0 && N > 0; i--){
        if(freq[i].empty()) continue;
        cout << i << nline;

        sort(freq[i].begin(), freq[i].end(), [](string a, string b) -> bool {
            if(a.length() != b.length()) return a.length() < b.length();
            else return a < b;
        });
        
        for(int j = 0; j < freq[i].size(); j++)
            cout << freq[i][j] << " \n"[(j+1)%6 == 0 || j == freq[i].size()-1];
        N--;
    }
}

int main() {
    read_input("contact");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}