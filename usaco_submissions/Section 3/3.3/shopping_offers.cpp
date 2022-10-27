#include <bits/stdc++.h>
using namespace std;

/*
TASK: shopping
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long
#define nline "\n"

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

struct offer{
    int items[5] = {0};
    int p;
};

int noffers, nitems;
vector<offer> offers;
int how_many[5];
int price[5];
int dp[6][6][6][6][6][100];

int c = 1;
unordered_map<int, int> hm;
int getUniqId(int x){
    if(hm[x]) return hm[x] - 1;
    hm[x] = c++;
    return hm[x] - 1;
}

/* debug routine */
void dbg(){
    cout << "items reqd. \n";
    for(int i = 0; i < 5; i++)
        cout << how_many[i] << " \n"[i == 4];

    cout << "special offers \n";
    for(int i = 0; i < noffers; i++){
        offer so = offers[i];
        for(int j = 0; j < 5; j++)
            cout << so.items[j] << " \n"[j == 4];
        cout << "price : " << so.p << nline;
    }
}

void solve(){
    cin >> noffers;
    for(int i = 0; i < noffers; i++){
        int n; cin >> n;
        int c, k;
        offer so;
        for(int j = 0; j < n; j++){
            cin >> c >> k;
            int id = getUniqId(c);
            so.items[id] = k;
        }
        cin >> so.p;
        offers.push_back(so);
    }

    cin >> nitems;
    int c, k, p;
    for(int i = 0; i < nitems; i++){
        cin >> c >> k >> p;
        int id = getUniqId(c);
        how_many[id] = k;
        price[id] = p;
    }

    // dbg();

    // /* Main routine */
    for(int a = 0; a <= how_many[0]; a++)
    for(int b = 0; b <= how_many[1]; b++)
    for(int c = 0; c <= how_many[2]; c++)
    for(int d = 0; d <= how_many[3]; d++)
    for(int e = 0; e <= how_many[4]; e++){
        dp[a][b][c][d][e][0] = a*price[0] + b*price[1] + c*price[2] + d*price[3] + e*price[4];
        for(int s = 1; s <= noffers; s++){
            offer so = offers[s-1];
            int offer_price = so.p;
            dp[a][b][c][d][e][s] = dp[a][b][c][d][e][s-1]; // ignoring the current offer

            if(a-so.items[0] < 0 || b-so.items[1] < 0 || c-so.items[2] < 0 || d-so.items[3] < 0 || e-so.items[4] < 0) continue;
            
            dp[a][b][c][d][e][s] = min(dp[a][b][c][d][e][s], offer_price + dp[a-so.items[0]][b-so.items[1]][c-so.items[2]][d-so.items[3]][e-so.items[4]][s]);
        }
    }

    cout << dp[how_many[0]][how_many[1]][how_many[2]][how_many[3]][how_many[4]][noffers] << nline;
}

int main() {
    read_input("shopping");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}