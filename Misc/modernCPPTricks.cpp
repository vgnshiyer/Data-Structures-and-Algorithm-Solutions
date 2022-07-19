#include <bits/stdc++.h>
using namespace std;

// this is where i store interesting cpp tricks
int main(){
    // cool trick in matrix
    int j = 1, m = 3;
    cout<<" \n"[j == m]; // ' \n' is a char array with 2 elements
    // if j == m, a newline will be printed, else a whitespace is printed
    // can be used in matrix printing or pattern printing

    //instead of using 2 nested for loops, u can add rows and columns and iterate with this formula
    int n = 2, m = 2;
    int a[n][m] = {{1,1},{2,2}};
    for(int i = 0; i < (n+m); i++){            // gives row   gives col
        cout<<a[i/m][i%m]<<" \n"[i%m == m-1]; // [i/columns][i%columns]
    }


    // print 12 digits after decimal point
    double answer = 0;
    printf("%.12f",answer);


    return 0;
}