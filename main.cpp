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
const int N = 1e6;

set<ll> sieve(ll n){
    vector<bool> prime(n+1,true);
    set<ll> primes;
    prime[0] = prime[1] == false;
    
    // O(nlog(log(n))) // almost linear time complexity
    for(ll i = 2LL; i <= n; i++){
        if(prime[i]){
            primes.insert(i);
            for(ll j = i*i; j <= n; j += i){ // as i*i-1 would already be marked by multiple of other numbers
                prime[j] = false;
            }
        }
    }
    return primes;
}

bool is_perfect_square(ll n){
    double sqrt_n = sqrt(n);
    return sqrt_n == int(sqrt(n));
}

void solve(){
    int n; cin>>n;
    set<ll> s = sieve(N);
    ll x; 
    fo(i, n) {
        cin>>x;
        if(is_perfect_square(x) && s.find(int(sqrt(x))) != s.end()) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }
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