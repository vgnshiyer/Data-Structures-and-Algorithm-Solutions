#include <bits/stdc++.h>
using namespace std;

/*
AUTHOR: Vignesh Iyer
ID: vgnshiyer
LANG: C++
University of Mumbai
*/

#define fast_read() ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#define typeof(x) typeid(x).name()
#define fo(i,n) for(int i=0;i<n;i++)
#define ll long long
#define pb push_back
#define mp make_pair
#define sz(a) (int)a.size()
#define F first
#define S second
#define deb(x) cout << #x << "=" << x << endl
#define deb2(x, y) cout << #x << "=" << x << "," << #y << "=" << y << endl
#define deb_array(arr) for(auto x : arr){cout<<x<<", ";}  cout<<endl;
#define all(x) x.begin(), x.end()
#define sortall(x) sort(all(x))
#define nline "\n"
#define PI 3.1415926535897932384626
typedef pair<int, int>	pii;
typedef pair<ll, ll>	pll;
typedef vector<int>		vi;
typedef vector<ll>		vl;
typedef vector<pii>		vpii;
typedef vector<pll>		vpll;
typedef vector<vi>		vvi;
typedef vector<vl>		vvl;
// const int N = 1e6;
// const ll MOD = 998244353;
// const int INF = INT_MAX;

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

void solve(){
    ll n, k; cin >> n >> k;
    string s; cin >> s;
    ll c0 = 0, c1 = 0;
    for(char c : s) c == '0' ? ++c0 : ++c1;

    ll m = min(c1, c0);
    c0 -= m;
    c1 -= m;
    ll best = max(c1,c0);

    if(best == 0)
        cout << 0 << nline;
    else if(k >= best)
        cout << 1 << nline;
    else if(k == 0){
        cout << best << nline;
    }
    else{
        cout << best/k + (best%k != 0) << nline;
    }
}

int main() {
    fast_read();
    
    #ifndef ONLINE_JUDGE
    read_input("file");
    #endif

    ll tc = 1;
    cin>>tc;
    while(tc--)
        solve();
    return 0;
}