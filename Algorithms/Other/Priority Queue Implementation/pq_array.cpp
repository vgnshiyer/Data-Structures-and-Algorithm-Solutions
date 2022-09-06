#include <bits/stdc++.h>
using namespace std;

/*
AUTHOR: Vignesh Iyer
ID: vgnshiyer
LANG: C++
University of Mumbai
*/

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
typedef pair<int, int>	pii;
typedef pair<ll, ll>	pll;
typedef vector<int>		vi;
typedef vector<ll>		vl;
typedef vector<pii>		vpii;
typedef vector<pll>		vpll;
typedef vector<vi>		vvi;
typedef vector<vl>		vvl;
// const int N = 1e6;
// const ll MOD = 998244353;
// const int INF = INT_MAX;

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

int insert(vi &pq, int data, int &size){
    for(int i = 0; i <= size; i++){
        if(pq[i] < data){
            // shift all elements right
            int prev = pq[i];
            for(int j = i; j < size; j++){
                int next = pq[j+1];
                pq[j+1] = prev;
                prev = next;
            }
            pq[i] = data;
            size++;
            return i;
        }
    }
}

void solve(){
    int n; cin >> n;
    vi pq(501, 0);
    int size = 0;

    int idx[n+1];

    for(int i = 0; i < n; i++){
        int x; cin >> x;
        int id = insert(pq, x, size);
        idx[i] = id+1;
    }

    for(int i = 0; i < n; i++)
        cout << idx[i] << nline;
    for(int i = 0; i < n; i++)
        cout << pq[i] << " ";
    cout << nline;
}

int main() {
    fast_read();
    
    #ifndef ONLINE_JUDGE
    read_input("file");
    #endif

    ll tc = 1;
    // cin>>tc;
    while(tc--)
        solve();
    return 0;
}