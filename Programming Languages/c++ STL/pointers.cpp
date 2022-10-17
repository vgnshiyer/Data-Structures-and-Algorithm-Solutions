#include <bits/stdc++.h>
using namespace std;



int main(){
    int a[] = {1 ,2, 3, 4, 5};
    int *p; // declare a pointer of type integer(which means the pointer will contain the address of an integer)
    p = &a[0]; // passing a reference of the first element to the pointer
    cout<<p<<endl; //printing the address of the first value in the array
    cout<<*p<<endl; // printing the value in the address by dereferencing with a asterisk*.
    p++; // incrementing the address
    cout<<*p<<endl; // printing the element in the next address

    int y = *p; // integer y is set to the integer pointed by p
    cout<<y<<endl;

    // can also do something fancy like this
    cout<<*(&a[2])<<endl; // deference the address by giving a reference to the third element in the array
    return 0;
}