#include <bits/stdc++.h>
using namespace std;

// MEX is the smallest positive number which does not belong to the array
int getMex(vector<int> a){
    sort(a.begin(), a.end()); // use set instead to avoid sorting TC
    int mex = 0;
    for(auto x : a){
        if(x == mex)
            mex++;
    }
    return mex;
}

int main(){
    vector<int> a = {0,2,1,5,3};
    cout<<getMex(a);
    return 0;
}