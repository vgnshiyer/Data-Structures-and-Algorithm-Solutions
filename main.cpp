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
typedef pair<int, int>	pii;
typedef pair<ll, ll>	pll;
typedef vector<int>		vi;
typedef vector<ll>		vl;
typedef vector<pii>		vpii;
typedef vector<pll>		vpll;
typedef vector<vi>		vvi;
typedef vector<vl>		vvl;

bool testcases = 1;

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

int n;
vi visited;

int get_min_distance(pii curr_pos, vpii a){
    int min_dist = INT_MAX;
    for(int i = 0; i < n; i++){
        if(visited[i]) continue;
        int dist = abs(curr_pos.F - a[i].F) + abs(curr_pos.S - a[i].S);
        min_dist = min(min_dist, dist);
    }
    if(min_dist == INT_MAX) return (abs(curr_pos.F) + abs(curr_pos.S));
    return min_dist;
}

int get_next_pos(pii curr_pos, vpii a){
    int min_dist = INT_MAX, min_idx = -1;
    pii ans;
    for(int i = 0; i < n; i++){
        if(visited[i]) continue;
        int dist = abs(curr_pos.F - a[i].F) + abs(curr_pos.S - a[i].S);
        if(dist < min_dist){
            min_dist = dist;
            ans = a[i];
            min_idx = i;
        }
    }
    if(min_dist == INT_MAX) return {0,0};
    visited[min_idx] = 1;
    return ans;
}

void solve(){
    cin >> n;
    vpii a(n);
    visited.resize(n, 0);
    for(int i = 0; i < n; i++) cin >> a[i].F >> a[i].S;

    int moves = 0;
    int dist = 0;
    pii curr_pos = {0,0};
    while(moves <= n){
        dist += get_min_distance(curr_pos, a);
        curr_pos = get_next_pos(curr_pos, a);
        moves++;
    }

    cout << dist << nline;
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