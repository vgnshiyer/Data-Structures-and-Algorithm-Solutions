#include <bits/stdc++.h>
using namespace std;

// -- JAI SHREE RAM -- 

#define fast_read() ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#define ll long long
#define deb(x) cout << #x << "=" << x << endl
#define deb2(x, y) cout << #x << "=" << x << "," << #y << "=" << y << endl
#define deb_array(arr) for(auto x : arr){cout<<x<<" ";}  cout<<endl;
#define all(x) x.begin(), x.end()
#define sortall(x) sort(all(x))
#define nline "\n"

bool testcases = 0;

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

void bruteForce(){
    
}

// we track the distance from both the nodes to their lowest common ancestors.. and count the number of steps
ll dist(ll a, ll b){
    if(a == b) return 0;

    if(a > b) swap(a, b);
    return 1 + dist(a, b/2);
}

void solve(){
    int n; cin >> n;
    ll x, y;
    for(int i = 0; i < n; i++){
        cin >> x >> y;
        cout << dist(x, y) << nline;
    }
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