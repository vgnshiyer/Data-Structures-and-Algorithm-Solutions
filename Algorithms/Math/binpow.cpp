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

int binpowm(int a, int b, int m){
    if(b==0)
        return 1;
    a %= m;
    int res = binpowm(a,b/2,m);
    if(b%2)
        return res*res*a % m;
    return res*res % m;
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
ll binpow(ll a, ll b)
{
    ll ans=1;
    
    while(b>0)
    {
        if((b%2)==1){
            ans=(ans*a)%MOD;
        }
        b/=2;
        a=(a*a)%MOD;
    }
    return ans;
}