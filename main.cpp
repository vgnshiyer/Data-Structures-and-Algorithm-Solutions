#include <bits/stdc++.h>
using namespace std;

#define typeof(x) typeid(x).name()
#define fo(i,n) for(int i=0;i<n;i++)
#define ll long long
#define pb push_back
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

int main() {
    // makes I/O faster
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif

    int t; cin >>t;
    
    while(t--){
        int n, q;
        cin>>n>>q;
        int a[n];
        fo(i,n) cin>>a[i];
        sort(a,a+n,greater<int>());
        while(q--){
            int sum = 0;
            int query; cin>>query;
            int i = 0;
            int num = 0;
            while(sum < query && i < n){
                sum += a[i++];
                num++;
            }
            if(sum < query) cout<<-1<<endl;
            else cout<<num<<endl;
        }
    }
}

/* 
_ _ _ _ 


*/