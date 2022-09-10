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

int n;

void solve(){
    cin >> n;
    vector<ll> A1(n), A2(n);
    set<ll> P1, P2;
    for(int i = 0; i < n; i++){
        cin >> A1[i];
        P1.insert(A1[i]);
    }
    for(int i = 0; i < n; i++){
        cin >> A2[i];
        P2.insert(A2[i]);
    }

    vector<ll> s1(n), s2(n), s3(n);
    ll m1 = -1, m2 = -1, m3 = -1;
    for(int i = 0; i < n; i++){
        ll a = distance(P1.begin(), P1.find(A1[i]));
        ll b = distance(P2.begin(), P2.find(A2[i]));
        s1[i] = a;
        m1 = max(m1, s1[i]);
        s2[i] = b;
        m2 = max(m2, s2[i]);
        s3[i] = a+b;
        m3 = max(m3, s3[i]);
    }
    bool qualified[n] = {false};
    
    for(int i = 0; i < n; i++){
        if(s1[i] == m1) qualified[i] = true;
        if(s2[i] == m2) qualified[i] = true;
        if(s3[i] == m3) qualified[i] = true;
    }

    int cnt = 0;
    for(int i = 0; i < n; i++) if(qualified[i]) cnt++;
    cout << cnt << nline;
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