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

vector<ll> a;
int n;

void compute(ll sum, int max_len, int i, int &best){
    if(i >= n){
        best = min(best, max_len);
        return;
    }

    ll temp = 0;
    int len = 0;
    while(temp < sum){
        temp += a[i++];
        len++;
    }
    max_len = max(len, max_len);
    if(temp == sum){
        compute(sum, max_len, i+1, best);
    } else{
        return;
    }
}

void solve(){
    cin >> n;
    a.resize(n);
    for(int i = 0; i < n; i++) cin >> a[i];

    ll sum = 0;
    int best = n;
    for(int i = 0; i < n; i++){
        sum += a[i];
        compute(sum, i+1, i+1, best);
    }

    cout << best << nline;
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