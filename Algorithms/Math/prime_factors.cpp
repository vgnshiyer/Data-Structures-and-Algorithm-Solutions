#include <bits/stdc++.h>
using namespace std;

#define ll long long

bool is_prime[1000000];
void sieve(ll n){
    for(ll i = 0; i <= n; i++) is_prime[i] = 1;
    is_prime[0] = is_prime[1] = 0;

    for(ll i = 2; i <= n; i++){
        if(is_prime[i]){
            for(ll j = i*i; j <= n; j+=i){
                is_prime[j] = 0;
            }
        }
    }
}

bool __is_primes_generated__ = false;

vector<ll> primes;
void gen_primes(ll n){
    __is_primes_generated__ = true;
    sieve(n+1);
    for(ll i = 2; i <= n; i++) if(is_prime[i]) primes.push_back(i);
}

set<ll> gen_pfactors(ll n){
    if(!__is_primes_generated__){
        cerr << "generate primes pls!";
        exit(1);
    }
    set<ll> facs;

    for(ll i = 0; primes[i]*primes[i] <= n, i < primes.size(); i++){
        while(n % primes[i] == 0){
            n /= primes[i];
            facs.insert(primes[i]);
        }
    }
    if(n > 1) facs.insert(n);
    return facs;
}

int main(){
    gen_primes(1000);
    
    vector<ll> facs = gen_pfactors(5184);
    for(auto x : facs) cout << x << " ";
    return 0;
}