#include <bits/stdc++.h>
using namespace std;

void sieve(int n){
    vector<bool> prime(n+1,1);
    prime[0] = prime[1] == false;
    
    // O(nlog(log(n))) // almost linear time complexity
    for(int i = 2; i <= n; i++){
        if(prime[i]){
            for(int j = i*i; j <= n; j += i){ // as i*i-1 would already be marked by multiple of other numbers
                prime[j] = false;
            }
        }
    }
}