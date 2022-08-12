#include <bits/stdc++.h>
using namespace std;

/*
TASK: combo
USER: Vignesh Iyer
LANG: C++
*/

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

int ans = 0;
int n;
int farmer[3], master[3];

bool isValid(int a, int b, int c, int key[]){
    int diff1 = abs(a - key[0]);
    int diff2 = abs(b - key[1]);
    int diff3 = abs(c - key[2]);
    bool valid = (diff1 <= 2 || diff1 >= (n - 2)) && (diff2 <= 2 || diff2 >= (n - 2)) && (diff3 <= 2 || diff3 >= (n - 2));
    return valid;
}

void solve(){
    cin >> n;
    for(int i = 0; i < 3; i++) cin >> farmer[i];
    for(int i = 0; i < 3; i++) cin >> master[i];

    for(int a = 1; a <= n; a++){
        for(int b = 1; b <= n; b++){
            for(int c = 1; c <= n; c++){
                if(isValid(a,b,c,farmer) || isValid(a,b,c,master)) ans++;
            }
        }
    }
    cout << ans << "\n";
}

int main() {
    read_input("combo");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}