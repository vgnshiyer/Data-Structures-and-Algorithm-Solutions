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
vi a;
int med;
priority_queue<double> s;
priority_queue<double,vector<double>,greater<double>> g;

int get_median(int x, int pos){
    if(pos == 1){
        s = priority_queue<double>(); // reset priority queue
        g = priority_queue<double,vector<double>,greater<double>>();
        med = x;
        s.push(x);
        return med;
    }
    if (s.size() > g.size()){
        if (x < med){
            g.push(s.top());
            s.pop();
            s.push(x);
        }
        else
            g.push(x);
        med = min(s.top(),g.top());
    }
    else if (s.size()==g.size()){
        if (x < med){
            s.push(x);
            med = s.top();
        }
        else{
            g.push(x);
            med = g.top();
        }
    }
    else{
        if (x > med){
            s.push(g.top());
            g.pop();
            g.push(x);
        }
        else
            s.push(x);
        med = min(s.top(), g.top());
    }
    return med;
}

bool is_valid(vi arr){
    int p1 = get_median(arr[0], 1);

    for(int i = 1; i < n-1; i++){
        int p2 = get_median(arr[i], 0);
        if(p1 == p2) return false;
        p1 = p2;
    }
    return true;
}

void solve(){
    cin >> n;
    a.resize(n);
    for(int i = 1; i <= n; i++) a[i-1] = i;

    do{
        if(is_valid(a)){
            deb_array(a);
            return;
        }
    }while(next_permutation(all(a)));
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