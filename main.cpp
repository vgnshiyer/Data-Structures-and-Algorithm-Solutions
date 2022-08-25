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

const ll MOD = 7 + 1e9;
bool testcases = 1;

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

ll n;
typedef vector<ll> vl;

void solve(){
    cin >> n;
    vl A(n), B(n);
    vl diffs;
    for(int i = 0; i < n; i++) cin >> A[i];
    for(int i = 0; i < n; i++){
        cin >> B[i];
        if(abs(A[i] - B[i]) > 0) diffs.pb(abs(A[i] - B[i]));
    }

    sortall(diffs);
    int N = sz(diffs);
    vl pref(N);
    ll prev = 0;
    for(int i = 0; i < N; i++){
        pref[i] = diffs[i];
        if(i) pref[i] += pref[i-1];
    }
    if(N == 0){
        cout << 0 << nline;
        return;
    }
    if(N == 1){
        cout << -1 << nline;
        return;
    }
    if(pref[N-1]%pref[N-2] == 0 && pref[N-1]/pref[N-2] == 2){
        cout << diffs[N-1] << nline;
        return;
    }
    cout << -1 << nline;
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