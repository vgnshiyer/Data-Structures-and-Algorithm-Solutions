#include <bits/stdc++.h>
using namespace std;

/*
TASK: beads
USER: Vignesh Iyer
LANG: C++
*/

#define nline "\n"
#define ll long long

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

int N;
char beads[800];

void solve(){
    int left[800][2];
    int right[800][2];

    cin >> N;
    for(int i = 0; i < N; i++) cin >> beads[i];
    for(int i = 0; i < N; i++) beads[i+N] = beads[i];
    N *= 2;

    left[0][0] = 0, left[0][1] = 0;
    for(int i = 1; i <= N; i++){
        if(beads[i-1] == 'r'){
            left[i][0] = left[i-1][0] + 1;
            left[i][1] = 0;
        } else if(beads[i-1] == 'b'){
            left[i][1] = left[i-1][1] + 1;
            left[i][0] = 0;
        } else {
            left[i][0] = left[i-1][0] + 1;
            left[i][1] = left[i-1][1] + 1;
        }
    }

    right[N][0] = 0, right[N][1] = 0;
    for(int i = N-1; i >= 0; i--){
        if(beads[i] == 'r'){
            right[i][0] = right[i+1][0] + 1;
            right[i][1] = 0;
        } else if(beads[i] == 'b'){
            right[i][1] = right[i+1][1] + 1;
            right[i][0] = 0; 
        } else{
            right[i][0] = right[i+1][0] + 1;
            right[i][1] = right[i+1][1] + 1;
        }
    }

    int ans = -1;
    for(int i = 0; i < N; i++){
        ans = max(ans, max(left[i][0], left[i][1]) + max(right[i][0], right[i][1]));
    }
    cout << min(ans, N/2) << nline;
}

int main(){
	read_input("beads");
	
	solve();
	return 0;
}