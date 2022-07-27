#include <bits/stdc++.h>
using namespace std;

/*
Below program is a non-recursive algorithm to print the kth permutation
of a sequence.
For the string s of length n, for any k from 0 to n! - 1 inclusive, the following modifies s to provide a unique permutation (that is, different from those generated for any other k value on that range). To generate all permutations, run it for all n! k values on the original value of s.

https://en.wikipedia.org/wiki/Permutation#Unordered_generation
*/

string permute(int k, string s){
    for(int j = 1; j < s.size(); j++){
        swap(s[k%(j+1)],s[j]);
        k = k/(j+1);
    }
    return s;
}

int main(){
    string s = "abc";
    for(int i = 0; i < 6; i++){
        string temp = permute(i, s);
        cout << temp << endl;
    }
    return 0;
}