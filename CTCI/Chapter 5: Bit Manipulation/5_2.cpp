// real number binary to string

#include<bits/stdc++.h>
using namespace std;

/*
How to convert real number to binary
1. multiply the fractional part by 2
2. if the result is greater than 1, append 1 to the result
3. else append 0
4. repeat steps 1 through 3 until we get a 0 in the fractional part
*/

void binaryToString(double num) {
    if(num > 1 || num < 0){
        cout << "ERROR" << endl;
        return;
    }

    string result = "0.";
    while(num > 0) {
        if(result.length() >= 32){
            // cout << "ERROR" << endl;
            break;
        }

        double r = num * 2;
        if(r > 1){
            result += "1";
            num = r - 1;
        } else {
            result += "0";
            num = r;
        }
    }
    cout << result << endl;
}

int main(){
    binaryToString(0.11);
    return 0;
}