#include <bits/stdc++.h>
using namespace std;

// if i divides n, n/i also divides n
int factors(int n){
    int count = 2;
    for(int i = 2; i*i <= n; i++){
        if(n%i == 0){
            count++;
            if(i != n/i)
                count++;
        }
    }
    return count;
}

//print divisors of first n numbers
void divisors_of_n(int n){
    vector<int> div(n+1);
    // O(nlogn) time
    for(int i = 1; i <= n; i++){
        for(int j = i; j <= n; j += i){
            div[j]++;
        }
    }
    for(int i = 1; i <= n; i++){
        cout<<div[i]<<endl;
    }
}