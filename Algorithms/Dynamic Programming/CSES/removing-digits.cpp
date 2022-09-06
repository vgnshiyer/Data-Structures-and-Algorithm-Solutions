/*
You are given an integer n. On each step, you may subtract one of the digits from the number.

How many steps are required to make the number equal to 0?

eg: 27
o/p: 5 (27 -> 20 -> 18 -> 10 -> 9 -> 0)
*/

#include<bits/stdc++.h>
using namespace std;

int dp[1000001];

int remove_digits_iterative(int n){
    dp[0] = 0;
 
    for(int i = 1; i <= n; i++){
        int num = i;
        int best = INT_MAX;
        while(num){
            int d = num % 10;
            num /= 10;
            if(d == 0) continue;
            best = min(best, 1 + dp[i-d]);
        }
        dp[i] = best;
    }
    return dp[n];
}

int remove_digits_recursive(int n){
    if(n == 0) return 0;
  
    int best = INT_MAX;
    int num = n;
    while(n){
        int d = n%10;
        n/=10;
        if(d == 0) continue;
        best = min(best,1 + remove_digits_recursive(num - d));
    }
  return best;
}

int main(){
    int n; cin >> n;
    cout << remove_digits_iterative(n) << endl;
    cout << remove_digits_recursive(n) << endl;
}