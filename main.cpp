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

/*
Dividing X by 2^y is equivalent to right shifting X by y bits. 
In order to make X as the minimum number, We want to unset the rightmost 1, from the index 1.(As xor of a number with itself is 0, we cannot take 0 as the answer. As the question says we need to do atleast 1 shift.)
Therefore we count the distance of the 1st set bit from the index 0.

eg. 

111010101
^111010101
-------------
100111111 (min val) It can be proved that any other computation will not give a smaller val
*/

void solve(){
    int n; cin >> n;
    char bits[n]; cin >> bits;

    int y = 1; // at least 1 shift has to be made
    for(int i = 1; i < n; i++){
        if(bits[i] == '1') break;
        y++;
    }
    cout << y << nline;
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