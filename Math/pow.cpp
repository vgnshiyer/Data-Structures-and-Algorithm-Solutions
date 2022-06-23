#include <bits/stdc++.h>
using namespace std;

// exponent in recursive form
int binpow(int a, int b){
    if(b==0)
        return 1;
    int res = binpow(a,b/2);
    if(b%2)
        return res*res*a;
    return res*res;
}

// exponent in iterative form
int binpow2(int a, int b){
    int res = 1;
    while(b != 0){
        if(b&1)
            res *= a;
        a *= a;
        b >>= 1;
    }
    return res;
}

//exponent modulo
int binpow3(int a, int b, int m){
    a %= m;
    int res = 1;
    while(b != 0){
        if(b&1)
            res *= a%m;
        a *= a%m;
        b >>= 1;
    }
    return res;
}