#include <bits/stdc++.h>
using namespace std;
//Using eucleadians algo
int gcd1(int a, int b) {
    if (b == 0)
        return a;
    else
        return gcd (b, a % b);
}

//using ternary operator
int gcd2(int a, int b) {
    return b ? gcd (b, a % b) : a;
}

int lcm (int a, int b) {
    return a / gcd2(a, b) * b;
}