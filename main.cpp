#include <bits/stdc++.h>
using namespace std;

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

int getAPDiff(vi a){
    int n = sz(a);
    if(n==1) return 0;
    int diff = a[1]-a[0];
    for(int i = 2; i < n; i++){
        if(a[i]-a[i-1] != diff) return -1;
    }
    return diff;
}

int main() {
    // makes I/O faster
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif

    string s; cin>>s;
    int n = sz(s);
    vi a(n, 0);
    fo(i, n){
        a[s[i] - 'a']++;
    }
    int oddCount = 0;
    fo(i, sz(a)){
        if(a[i]%2 == 1){
            oddCount++;
        }
    }
    if(oddCount == 0 || oddCount%2 == 1)
        cout<<"First"<<endl;
    else
        cout<<"Second"<<endl;
}