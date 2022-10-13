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

const ll MOD = 998244353;
bool testcases = 1;

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

ll binpow(ll a, ll b)
{
    ll ans=1;
    
    while(b>0)
    {
        if((b%2)==1){
            ans=(ans*a)%MOD;
        }
        b/=2;
        a=(a*a)%MOD;
    }
    return ans;
}

ll getCount(ll m, ll i){
    ll ans = ((m >> (i+1)) << i);
    if((m >> i) & 1) 
        ans += (m & ((1 << i) - 1));
    return ans;
}

void solve(){
    ll n, m;
    cin >> n >> m;

    ll ans = 0;
    for(int i = 0; i <= 32; i++){
        if((1 << i) > m) break;
        ll p = getCount(m+1, i);
        p = binpow(p, n);
        ans=(ans+((p*(1 << i))%MOD))%MOD;
    }
    cout << ans << nline;
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