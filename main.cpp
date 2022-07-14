#include <bits/stdc++.h>
using namespace std;

#define fast_read() ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define typeof(x) typeid(x).name()
#define fo(i,n) for(int i=1;i<=n;i++)
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
// const ll MOD = 1e9 + 7;
// const int INF = INT_MAX;

void solve(){
    int n; cin >> n;
    map<ll, int> hm;
    ll x;
    ll loners = 0;
    ll mx;
    fo(i, n) {
        cin >> x;
        hm[x]++;
        mx = max(mx, x);
    }
    int maxcount = 0;
    for(pair<ll, int> a : hm){
        if(a.S == 1) loners++;
        maxcount = max(maxcount, a.S);
    }
    ll res = (loners/2) + (loners%2);
    if(hm[mx] == 1 && maxcount == 2) res++;
    cout << res << endl;
}

int main() {
    fast_read();

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif

    int t; cin>>t;
    while(t--){
        solve();
    }
    return 0;
}