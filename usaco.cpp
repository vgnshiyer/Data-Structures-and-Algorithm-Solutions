#include <bits/stdc++.h>
using namespace std;

/*
TASK: ride
USER: Vignesh Iyer
LANG: C++
*/

long long get_product(string a){
    long long ans = 1;
    for(char c : a){
        ans *= (long long)(c-'A' + 1);
    }
    return ans;
}

void solve(){
    string a, b;
    cin >> a >> b;
    long long prod1 = get_product(a), prod2 = get_product(b);
    if(prod1%47 == prod2%47)
        cout << "GO" << endl;
    else
        cout << "STAY" << endl;
}

int main() {
    freopen("ride.in", "r", stdin);
    freopen("ride.out", "w", stdout);

    solve();

    return 0;
}