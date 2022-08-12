#include <bits/stdc++.h>
using namespace std;

/*
TASK: sprime
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long
#define nline "\n"

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

ll n;
ll prime_makers[] = {1,2,3,5,7,9};

bool is_prime(ll n){
    if(n <= 1) return false;
    if(n <= 3) return true;

    if(n%2 == 0 || n % 3 == 0) return false;

    for(ll i = 5; i*i <= n; i += 6)
        if(n%i == 0 || n % (i+2) == 0) return false;

    return true;
}

void compute(ll num, ll len){
    if(len == n){
        cout << num << nline;
        return;
    }

    num *= 10;
    for(auto prime : prime_makers){
        num += prime;
        if(is_prime(num)) compute(num, len+1);
        num -= prime;
    }
}

void solve(){
    cin >> n;
    compute(0, 0);
}

int main() {
    read_input("sprime");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}