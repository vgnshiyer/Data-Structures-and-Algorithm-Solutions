#include <bits/stdc++.h>
using namespace std;

// if i divides n, n/i also divides n
int factors(int n){
    int count = 2;
    for(int i = 2; i*i < n; i++){
        if(n%i == 0)
            count++;
        if(i != n/i)
            count++;
    }
    return count;
}