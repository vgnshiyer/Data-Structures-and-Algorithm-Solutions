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
bool testcases = 0;

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

int R, C, cnt = 0;
string tgt;

void check(vector<vector<char>> mat, int i, int j, int len){
    if(len == tgt.length()){
        cnt++;
        return;
    }
    if(i < 0 || i >= R || j < 0 || j >= C || mat[i][j] != tgt[len]) return;

    char curr_char = mat[i][j];
    mat[i][j] = '#';
    check(mat, i+1, j, len+1);
    check(mat, i-1, j, len+1);
    check(mat, i, j+1, len+1);
    check(mat, i, j-1, len+1);
    mat[i][j] = curr_char;
}

void solve(){
    cin >> R >> C;
    vector<vector<char>> mat(R, vector<char>(C));
    for(int i = 0; i < R; i++)
    for(int j = 0; j < C; j++)
        cin >> mat[i][j];
    cin >> tgt;

    for(int i = 0; i < R; i++)
    for(int j = 0; j < C; j++){
        if(mat[i][j] == tgt[0])
            check(mat, i, j, 0);
    }
    cout << cnt/4 << nline;
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