#include <bits/stdc++.h>
using namespace std;

bool is_prime1(int n){
    if(n <= 1) return false;
    if(n == 2) return true;
    
    for(int i = 2; i*i <= n; i++)
        if(n % i == 0) return false;
    return true;
}

bool is_prime2(int n){
    if(n <= 1) return false;
    if(n <= 3) return true;
    if(n % 2 == 0) return false;

    for(int i = 3; i*i <= n; i += 2)
        if(n % i == 0) return false;
    return true;
}

bool is_prime3(ll n){
    if(n <= 1) return false;
    if(n <= 3) return true;

    if(n%2 == 0 || n % 3 == 0) return false;

    for(ll i = 5; i*i <= n; i += 6)
        if(n%i == 0 || n % (i+2) == 0) return false;

    return true;
}

int main(){
    is_prime1(13);
    return 0;
}