#include <bits/stdc++.h>
using namespace std;

void insertion_sort(vector<int>& arr, int n){
    for(int i = 0; i < n; i++){
        int cur = arr[i];
        cout << "\n Iteration number " << i << endl;
        for(int x : arr) cout << x << " ";
        cout << endl;
        int j = i-1;
        for(; j >= 0 && cur <= arr[j] ; j--)
            arr[j+1] = arr[j]; // shift the previous elements greater than curr, one position forward
        arr[j+1] = cur; // place cur to its appropriate position
        cout << "Placing " << cur << " to its position\n";
        for(int x : arr) cout << x << " ";
        cout << endl;
    }   
}

void insertion_sort_recursive(vector<int>& arr, int n) {
    if(n <= 1) return;
    insertion_sort_recursive(arr, n - 1);
    cout << "\n Iteration number " << n << endl;
    for(int x : arr) cout << x << " ";
    cout << endl;
    int last = arr[n - 1];
    int j = n - 2;
    for(; j >= 0 && last < arr[j]; j--)
        arr[j + 1] = arr[j];
    arr[j + 1] = last;
    cout << "Placing " << last << " to its position\n";
    for(int x : arr) cout << x << " ";
    cout << endl;
}

int main(){
    vector<int> arr = {12, 45, 8, 15, 33};

    cout << "Array before sorting..\n";
    for(int x : arr) cout << x << " ";
    cout << endl;

    cout << "\nInsertion sort visualization : \n";

    insertion_sort(arr, 5);

    cout << "\nInsertion sort visualization for recursive version: \n";

    arr = {12, 45, 8, 15, 33};

    insertion_sort_recursive(arr, 5);

    cout << "\n Array after sorting..\n";
    for(int x : arr) cout << x << " ";
    cout << endl;

    return 0;
}