#include <bits/stdc++.h>
using namespace std;

// -- JAI SHREE RAM -- 

#define fast_read() ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#define typeof(x) typeid(x).name()
#define ll long long
#define pb push_back
#define mp make_pair
#define sz(a) (int)a.size()
#define F first
#define S second
#define deb(x) cout << #x << "=" << x << endl
#define deb2(x, y) cout << #x << "=" << x << "," << #y << "=" << y << endl
#define deb_array(arr) for(auto x : arr){cout<<x<<" ";}  cout<<endl;
#define all(x) x.begin(), x.end()
#define sortall(x) sort(all(x))
#define nline "\n"
#define PI 3.1415926535897932384626

const ll MOD = 7 + 1e9;
bool testcases = 0;

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

vector<vector<int>> dp;

int compute(vector<int> coins, int s, int i){
    if(s == 0) return 1;
    if(i < 0) return 0;

    int &ans = dp[s][i];
    if(ans != -1) return ans;
    int res = 0;
    if(coins[i] <= s)
        res += compute(coins, s - coins[i], i);
    res += compute(coins, s, i-1);
    return ans = res;
}

void solve(){
    int n, s; cin >> n >> s;
    vector<int> coins(n);
    dp.resize(s+1, vector<int>(n+1, -1));
    for(int i = 0; i < n; i++) cin >> coins[i];
    cout << compute(coins, s, n-1) << nline;
}

int main() {
    fast_read();
    
    #ifndef ONLINE_JUDGE
    read_input("file");
    #endif

    ll tc = 1;
    if(testcases) cin>>tc;
    while(tc--)
        solve();
    return 0;
}