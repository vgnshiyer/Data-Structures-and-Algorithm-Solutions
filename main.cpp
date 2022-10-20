#include <bits/stdc++.h>
using namespace std;

// -- JAI SHREE RAM -- 

#define fast_read() ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#define ll long long
#define deb(x) cout << #x << "=" << x << endl
#define deb2(x, y) cout << #x << "=" << x << "," << #y << "=" << y << endl
#define deb_array(arr) for(auto x : arr){cout<<x<<" ";}  cout<<endl;
#define all(x) x.begin(), x.end()
#define sortall(x) sort(all(x))
#define nline "\n"
const ll MOD = 998244353;

bool testcases = 1;

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}


void solve(){
    int n; cin >> n;
    int a[n];
    int zero = 0, one = 0, sum = 0;
    for(int i = 0 ; i < n; i++){
        cin >> a[i];
        (a[i] == 0 ? zero++ : one++);
    }

    sum += min(zero, one);
    if(one > zero){
        int rem = max(zero, one) - min(zero, one);
        sum += rem/3;
    } 
    cout << sum << nline;
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