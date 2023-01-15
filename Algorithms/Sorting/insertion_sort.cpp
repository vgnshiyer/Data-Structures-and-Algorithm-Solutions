#include <bits/stdc++.h>
using namespace std;

int main(){
    int arr[5] = {12, 45, 8, 15, 33};

    cout << "Array before sorting..\n";
    for(int x : arr) cout << x << " ";
    cout << endl;

    cout << "\nInsertion sort visualization : \n";

    for(int i = 0; i < 5; i++){
        int cur = arr[i];
        for(int x : arr) cout << x << " ";
        cout << endl;
        int j = i-1;
        for(; j >= 0 && cur <= arr[j] ; j--)
            arr[j+1] = arr[j]; // shift the previous elements greater than curr, one position forward
        arr[j+1] = cur; // place cur to its appropriate position
        cout << "Placing cur to its position\n";
        for(int x : arr) cout << x << " ";
        cout << endl;
    }

    cout << "Array after sorting..\n";
    for(int x : arr) cout << x << " ";
    cout << endl;

    return 0;
}