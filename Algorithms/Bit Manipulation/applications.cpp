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
    cout << endl;
}

int num_of_ones(int n){
    int cnt = 0;
    while(n){
        n &= (n-1);
        cnt++;
    }
    return cnt;
}

uint32_t reverseBits(uint32_t n) {
    uint32_t answer = 0;
    
    for(int i = 31; i >= 0; i--)
        if(n & (1 << i)) answer |= (1 << (31-i));
    binary_representation(int(answer));
    return answer;
}

int main(){
    // following prints the binary representation of the number 22
    binary_representation(24); // 00000000000000000000000000010110
    cout << num_of_ones(5) << endl; // 2 (0101)
    cout << "(" << reverseBits(uint32_t(24)) << ")x" << endl;
    return 0;
}