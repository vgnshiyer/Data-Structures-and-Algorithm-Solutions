#include<stdio.h>
#include <bits/stdc++.h>
using namespace std;

void print_move(int start, int end){
    cout << start << "->" << end << endl;
}

void hanoi(int n, int start, int end){
    if(n == 1){
        print_move(start, end);
        return;
    }

    int other = 6 - (start + end);
    hanoi(n-1, start, other);
    print_move(start, end);
    hanoi(n-1, other, end);
}

int main(){
    hanoi(3, 1, 3);
    return 0;
}