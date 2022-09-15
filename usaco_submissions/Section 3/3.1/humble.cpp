#include <bits/stdc++.h>
using namespace std;

/*
TASK: humble
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long
#define nline "\n"

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

int n, k;
vector<int> primes;
vector<int> humble;
vector<int> min_index;

void solve(){
    cin >> k >> n;
    primes.resize(k);
    min_index.resize(k);
    fill(min_index.begin(), min_index.end(), 0);
    
    for(int i = 0; i < k; i++) cin >> primes[i];
    
    humble.push_back(1);
    for(int i = 1; i <= n; i++){
        int minh = INT_MAX;
        for(int j = 0; j < k; j++){
            while(humble[min_index[j]] * primes[j] <= humble[i-1])
                min_index[j]++;
            if(humble[min_index[j]] * primes[j] > humble[i-1])
                minh = min(minh, humble[min_index[j]]*primes[j]);
        }
        humble.push_back(minh);
    }
    cout << humble[n] << nline;
}

int main() {
    read_input("humble");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}