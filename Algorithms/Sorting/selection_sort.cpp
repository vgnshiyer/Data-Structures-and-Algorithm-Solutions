#include <bits/stdc++.h>
using namespace std;

int main(){
    int arr[5] = {12, 45, 8, 15, 33};

    cout << "Array before sorting..\n";
    for(int x : arr) cout << x << " ";
    cout << endl;

    cout << "\nSelection sort visualization : \n";

    for(int i = 0; i < 5; i++){
        int min_possible = arr[i], min_idx = i;
        for(int x : arr) cout << x << " ";
        cout << endl;
        for(int j = i+1; j < 5; j++){
            if(arr[j] < min_possible){
                min_possible = arr[j];
                min_idx = j;
            }
        }
        cout << "swapping " << i << " and " << min_idx << endl;
        swap(arr[i], arr[min_idx]);
        for(int x : arr) cout << x << " ";
        cout << endl;
        cout << "placed " << i << "th element \n\n";
    }

    cout << "Array after sorting..\n";
    for(int x : arr) cout << x << " ";
    cout << endl;

    return 0;
}