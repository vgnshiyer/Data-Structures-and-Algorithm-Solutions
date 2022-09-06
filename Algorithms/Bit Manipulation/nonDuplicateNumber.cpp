#include <bits/stdc++.h>
using namespace std;

/*
Given a set of numbers, find the number which does not have a duplicate.

Using a hashmap, this problem can be easily solved with O(n) time and O(n) space.
But we can use the property of the XOR operation to solve it in O(n) time and O(1) space.
x^x = 0
0^x = x
*/

int main(){
    int a[] = {4,3,2,4,2,1,5,1,5};
    int x = 0;
    for(int i = 0; i < 9; i++){
        x ^= a[i];
    }
    cout << x << " is the answer"; // 3
    return 0;
}