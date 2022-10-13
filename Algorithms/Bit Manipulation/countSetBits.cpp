#include <bits/stdc++.h>
using namespace std;

int count(int m, int i){
    int ans = (m >> (i+1)) << i;
    if((m >> i) & 1)
        ans += (m & ((1 << i) - 1));
    return ans;
}

int main(){
    count(5, 3); // returns the count of numbers from 0 to 5-1, where the third bit is set.
}