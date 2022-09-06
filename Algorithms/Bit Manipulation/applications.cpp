#include <bits/stdc++.h>
using namespace std;

/*
A number of the form 1 << k has one bit in the kth position and all other bits as zero.
We can use such a number to access the kth bit of a number x.
Formally, kth bit of a number x, is exactly one when x&(1<<k) == 1.

It is also possible to modify the kth bit using x|(1<<k) => set the kth bit to 1.
Formula x~(1<<k) sets the kth bit to 0.
Formula x^(1<<k) inverts the kth bit.

*/

void binary_representation(int x){
    for(int i = 31; i >= 0; i--){
        if(x&(1<<i)) cout << 1;
        else cout << 0;
    }
}

int main(){
    // following prints the binary representation of the number 22
    binary_representation(22); // 00000000000000000000000000010110
    return 0;
}