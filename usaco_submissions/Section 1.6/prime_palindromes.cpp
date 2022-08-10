#include <bits/stdc++.h>
using namespace std;

/*
TASK: pprime
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long
#define nline "\n"

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

ll a, b;

bool is_prime(ll n){
    if(n <= 1) return false;
    if(n <= 3) return true;

    if(n%2 == 0 || n % 3 == 0) return false;

    for(ll i = 5; i*i <= n; i += 6)
        if(n%i == 0 || n % (i+2) == 0) return false;

    return true;
}

ll create_palindrome(int num, bool is_odd){
    ll p = num;

    if(is_odd) num /= 10;

    while(num){
        p = p*10 + num%10;
        num /= 10;
    }
    return p;
}

set<ll> generate_prime_palindromes(ll a, ll b){
    ll number;
    set<ll> palindrome_primes;

    for(int is_odd = 0; is_odd < 2; is_odd++){
        ll i = 1;
        while((number = create_palindrome(i, is_odd)) <= b){
            if(number >= a && is_prime(number)){
                palindrome_primes.insert(number);
            }
            i++;
        }
    }
    return palindrome_primes;
}

void solve(){
    cin >> a >> b;
    
    auto ans = generate_prime_palindromes(a, b);
    for(auto x : ans) cout << x << nline;
}

int main() {
    read_input("pprime");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}