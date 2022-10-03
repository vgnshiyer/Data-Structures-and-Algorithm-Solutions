#include <bits/stdc++.h>
using namespace std;

/*
TASK: fact4
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long
#define nline "\n"

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

int n;

/*
We need the last non zero digit. We can ignore all leading zeros by excluding the 2s and 5s from our product. And simply taking a module of the product by 10 at every iteration, so that we maintain the last non-zero digit.

At the end, we just need to multiply the remaining 2s after pairing all the 2s and 5s we could.
*/

void solve(){
    cin >> n;
    
    int n2 = 0, n5 = 0;
    int prod = 1;
    for(int i = 1; i <= n; i++){
        int num = i;
        while(num%2 == 0){
            n2++;
            num/=2;
        }
        while(num%5 == 0){
            n5++;
            num/=5;
        }
        prod *= num;
        prod %= 10;
    }

    for(int i = 0; i < n2-n5; i++) prod = (prod * 2) % 10;
    cout << prod << nline;
}   

int main() {
    read_input("fact4");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}