#include <bits/stdc++.h>
using namespace std;

bool is_prime[50000000];

vector<ll> sieve(ll start, ll end){
    end = (end - 1)/2;
    for(ll i = 0; i <= end; i++) is_prime[i] = 1;
    is_prime[0] = 0;

    vector<ll> primes;

    for(ll i = 1; i <= end; i++){
        if(is_prime[i]){
            ll num = 2*i + 1;
            if(num >= start)
                primes.push_back(num);
            ll start_idx = (num*num - 1)/2;
            for(ll j = start_idx; j <= end; j += num){
                is_prime[j] = 0;
            }
        }
    }
    return primes;
}

void solve(){
    cin >> a >> b;

    auto primes = sieve(a, b);
    for(auto x : primes) cout << x << nline;
}

int main() {
    solve();

    return 0;
}