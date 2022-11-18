#include <bits/stdc++.h>
using namespace std;

bool doesIntersect(int a1, int a2, int b1, int b2){
    /*  a1--------------a2
    b1-----------b2

        a1--------------a2
    b1-----------------------b2   */
    if (a1 >= b1 && a1 <= b2)
        return true;
    /*   b1-------------b2
    a1-----------a2

        b1-------------b2
    a1-----------------------a2   */
    if ((b1 >= a1 && b1 <= a2))
        return true;
    return false;
}

int main(){
    int a1 = 1, a2 = 5;
    int b1 = 2, b2 = 7;

    cout << doesIntersect(a1, a2, b1, b2);
    return 0;
}