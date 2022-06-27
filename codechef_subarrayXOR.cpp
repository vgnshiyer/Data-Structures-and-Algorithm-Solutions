#include <bits/stdc++.h>
using namespace std;

#define typeof(x) typeid(x).name()
#define fo(i,n) for(int i=0;i<n;i++)
#define ll long long
#define ull unsigned ll
#define pb push_back
#define mp make_pair
#define sz(a) (int)a.size()
#define F first
#define S second
#define deb(x) cout << #x << "=" << x << endl
#define deb2(x, y) cout << #x << "=" << x << "," << #y << "=" << y << endl
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

void solve(){
    int n, k; cin>>n>>k;
    vi a(n);
    fo(i, n) cin>>a[i];

    int currXOR = 0, lo, hi = 0;
    int minWindowSize = INT_MAX;
    fo(lo, n){
        while(currXOR < k && hi < n){
            currXOR ^= a[hi++];
        }
        if(currXOR >= k){
            minWindowSize = min(minWindowSize, (hi - lo));
        }
        currXOR ^= a[lo];
    }
    (minWindowSize == INT_MAX) ? cout<<-1<<endl : cout<<minWindowSize<<endl;
}

int main() {
    // makes I/O faster
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

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