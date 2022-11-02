#include <bits/stdc++.h>
using namespace std;

/*
TASK: range
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long
#define nline "\n"

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

int N;
int mat[251][251];
int gazing_areas[251];

void solve(){
    /* Input */
    cin >> N;
    for(int i = 0; i < N; i++)
    for(int j = 0; j < N; j++){
        char c;
        cin >> c;
        mat[i][j] = int(c - '0');
    }

    /* Main routine */
    for(int i = 1; i < N; i++)
    for(int j = 1; j < N; j++){
        if(mat[i][j] == 1)
            mat[i][j] = min({mat[i-1][j-1], mat[i-1][j], mat[i][j-1]}) + 1;
        
        for(int x = 0; x <= mat[i][j]; x++)
            gazing_areas[x]++;
    }

    /* Output */
    for(int i = 2; i <= N; i++){
        if(gazing_areas[i])
            cout << i << " " << gazing_areas[i] << nline;
    }
}

int main() {
    read_input("range");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}