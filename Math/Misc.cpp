#include <bits/stdc++.h>
using namespace std;

bool is_perfect_square(int n){
    float sqrt_n = sqrt(n);
    return sqrt_n == int(sqrt(n));
}

/*
Modulo operator fomulas
Modular arithmetic is used to prevent overflow of numbers in case of large computations
(a+b)%m = (a%m + b%m)%m
(a*b)%m = (a%m * b%m)%m
(a+b)%m = (a%m - b%m + m)%m to prevent negative numbers // eg. (7-2)%3 = (1-2)%3 = -1 thats why we add m
*/

// a/b % m cannot be computed directly for huge numbers
// we modulo a. find the multiplicative inverse for b and multiply it by the new a. Finally take the modulo.
// eg 6/2%5 == 1/inv(2) % 5
// inv of 2 is 3
// ans : 3
// two numbers are multiplicative inverse of each other means, when u multiple each other, you get 1.
// with modulo, a*b % 5 should be 1
// eg. 2*x%5 = 1 :-- 2*3%5 = 1.. therefore, inv(2) = 3
int multiplicative_inverse(int a,int b, int m){ // only works if m is prime
    a %= m;
    int inv =  binpow(b,m-2,m); // fermat's little theorem
    return inv*a % m;
}

int binpow(int a, int b, int m){}