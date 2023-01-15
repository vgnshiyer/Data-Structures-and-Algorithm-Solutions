#include <bits/stdc++.h>
#include <stdio.h>
using namespace std;

int main(){
    int arr[5] = {12, 45, 8, 5, 16};

    cout << "Array before sorting..";
    for(int x : arr) cout << x << " ";
    cout << endl;

    cout << "\nBubble sort visualization : \n";
    for(int i = 0; i < 5; i++){
        for(int x : arr) cout << x << " ";
        cout << endl;
        for(int j = i; j < 5; j++){
            if(arr[j] < arr[i]){
                cout << "swapping " << i << " and " << j << endl;
                swap(arr[j], arr[i]);
                for(int x : arr) cout << x << " ";
                cout << endl;
            }
        }
        cout << "finished pass : " << i << endl; 
    }

    cout << "Array after sorting..";
    for(int x : arr) cout << x << " ";
    cout << endl;

    return 0;
}