#include <bits/stdc++.h>
using namespace std;

#define fast_read() ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
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
#define PI 3.1415926535897932384626
typedef pair<int, int>	pii;
typedef pair<ll, ll>	pll;
typedef vector<int>		vi;
typedef vector<ll>		vl;
typedef vector<pii>		vpii;
typedef vector<pll>		vpll;
typedef vector<vi>		vvi;
typedef vector<vl>		vvl;

int lens[3];
vi dp(5000, -1);

int getMaxRibbons(int n){
    if(n == 0) return 0;
    if(n < 0) return INT_MIN;
    int &ans = dp[n];
    if(ans != -1) return ans;
    return ans = max({getMaxRibbons(n-lens[0]) + 1, getMaxRibbons(n-lens[1]) + 1, getMaxRibbons(n-lens[2]) + 1});
}

void solve(){
    int n;cin>>n;
    fo(i, 3) cin>>lens[i];
    int ans = getMaxRibbons(n);
    cout<<ans<<endl;
}

int main() {
    fast_read();

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif

    // int t; cin>>t;
    // while(t--){
    solve();
    // }
    return 0;
}