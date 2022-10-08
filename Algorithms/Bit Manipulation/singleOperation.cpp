#include<bits/stdc++.h>
using namespace std;

/*
Chef has the binary representation S of a number X with him. He can modify the number by applying the following operation exactly once:

Make X:=X⊕⌊X/2^Y⌋, where (1 ≤ Y ≤ ∣S∣) and ⊕ denotes the bitwise XOR operation.
Chef wants to maximize the value of X after performing the operation. Help Chef in determining the value of Y which will maximize the value of X after the operation.

ANALYSIS:
* Dividing X by 2^y is equivalent to right shifting X by y bits.
* In order to make X as the maximum number, we want to keep as many bits at the rightmost part of the string as set.
* Therefore, the best way to do this is to shift the string to the right until we find the first 0.
* This way, all the rightmost bits will be set and the 0th bit will be set too.

111010101
^  111010101
-------------
111101111111 (max val) It can be proved that any other computation will not give a greater val
*/

void singleOper(vector<string> inp){
    for(string bits : inp){
        int y = 1;
        int n = bits.length();
        for(int i = 0; i < n; i++){
            y += (bits[i] == '1');
            if(bits[i] =='0') break;
        }
        cout << y << endl;
    }
}

/*
Similarly, to minimize the value,
* Dividing X by 2^y is equivalent to right shifting X by y bits. 
* In order to make X as the minimum number, We want to unset the rightmost 1, from the index 1.(As xor of a number with itself is 0, we cannot take 0 as the answer. As the question says we need to do atleast 1 shift.)
* Therefore we count the distance of the 1st set bit from the index 0.

eg. 

111010101
^111010101
-------------
100111111 (min val) It can be proved that any other computation will not give a smaller val

int y = 1; // at least 1 shift has to be made
    for(int i = 1; i < n; i++){
        if(bits[i] == '1') break;
        y++;
    }
    cout << y << nline;
*/

int main(){
    vector<string> inp = {"10", "11", "101", "110"};
    singleOper(inp);
    return 0;
}