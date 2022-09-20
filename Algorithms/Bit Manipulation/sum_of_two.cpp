#include <bits/stdc++.h>
using namespace std;

int main(){
    int a = 4, b = 5;

    // adding the numbers 
    // with bit manipulation
    while(b){
        int c = a&b;
        a ^= b;
        b = c << 1;
    }
    cout << a << endl;
}