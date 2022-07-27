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

bool is_prime[1000000];
void sieve(ll n){
    for(ll i = 0; i <= n; i++) is_prime[i] = 1;
    is_prime[0] = is_prime[1] = 0;

    for(ll i = 2; i <= n; i++){
        if(is_prime[i]){
            for(ll j = i*i; j <= n; j+=i){
                is_prime[j] = 0;
            }
        }
    }
}

bool __is_primes_generated__ = false;

vector<ll> primes;
void gen_primes(ll n){
    __is_primes_generated__ = true;
    sieve(n+1);
    for(ll i = 2; i <= n; i++) if(is_prime[i]) primes.push_back(i);
}

vector<ll> gen_pfactors(ll n){
    if(!__is_primes_generated__){
        cerr << "generate primes pls!";
        exit(1);
    }
    vector<ll> facs;

    for(ll i = 0; primes[i]*primes[i] <= n, i < primes.size(); i++){
        if(n % primes[i] == 0){
            while(n % primes[i] == 0){
                n /= primes[i];
                facs.push_back(primes[i]);
            }
        }
    }
    if(n > 1) facs.push_back(n);
    sort(facs.begin(), facs.end());
    return facs;
}

void solve(){
    ll n; cin >> n;
    gen_primes(2e3);

    vl facs = gen_pfactors(n);

    unordered_map<ll, ll> cnt;
    for(auto x : facs) ++cnt[x];

    ll highest_power = 0;
    for(auto p : cnt) highest_power = max(highest_power, p.S);

    ll b = 0;
    while((1 << b) < highest_power) ++b;

    ll ops = b;
    bool all_same = 1;
    for(auto p : cnt) if(p.S != (1 << b)) all_same = false;

    if(!all_same) ++ops;

    ll ans = 1;
    for(auto p : cnt) ans *= p.F;

    cout << ans << " " << ops;
}

int main() {
    fast_read();
    
    #ifndef ONLINE_JUDGE
    read_input("file");
    #endif

    int tc = 1;
    // cin>>t;
    while(tc--)
        solve();
    return 0;
}