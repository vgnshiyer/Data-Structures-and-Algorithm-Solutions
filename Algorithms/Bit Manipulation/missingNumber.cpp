#include <bits/stdc++.h>
using namespace std;

int main(){
    int arr[5] = {0,1,3,2,5};

    int missing = 5;
    for(int i = 0; i < 5; i++){
        missing ^= i;
        missing ^= arr[i];
    }
    cout << missing << endl;
}