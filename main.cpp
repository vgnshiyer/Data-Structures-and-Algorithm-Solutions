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

int query(int element, int k, int n, int a[]){
    int numbers_after_k = 0, numbers_before_k = 0;
    for(int i = k; i < n; i++){
        if(a[i] != element)
            return -1;
        numbers_after_k++;
    }
    for(int j = k-2; j >= 0; j--){
        if(a[j] != element)
            break;
        numbers_before_k++;
    }
    return n-(numbers_after_k + numbers_before_k + 1);
}

void solve(){
    int n, k; cin>>n>>k;
    int a[n];
    fo(i,n){
        cin>>a[i];
    }
    int element = a[k-1];
    int ans = query(element,k,n,a);
    cout<< ans;
}

int main() {
    // makes I/O faster
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif

    solve();
    return 0;
}