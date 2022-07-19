#include <bits/stdc++.h>
using namespace std;

/*
AUTHOR: Vignesh Iyer
ID: vgnshiyer
LANG: C++
University of Mumbai
*/

#define fast_read() ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define typeof(x) typeid(x).name()
#define fo(i,n) for(i=0;i<n;i++)
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
// const ll MOD = 1e9 + 7;
// const int INF = INT_MAX;
ll n, i, j, a, b;

ll get_product(string a){
    ll ans = 1;
    for(char c : a){
        ans *= (ll)(c-'A' + 1);
    }
    return ans;
}

void solve(){
    string a, b;
    cin >> a >> b;
    ll prod1 = get_product(a), prod2 = get_product(b);
    if(prod1%47 == prod2%47)
        cout << "GO";
    else
        cout << "STAY";
}

int main() {
    fast_read();

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif

    // int t; cin>>t;
    // while(t--)
        solve();
    return 0;
}