#include <bits/stdc++.h>
using namespace std;

void printPermutations(string s, string ans){
    if(ans.size() == 4){
        cout<<ans<<endl;
        return;
    }
    for(int i = 0; i < s.size(); i++){
        if(s[i] != '_'){
            char currChar = s[i];
            s[i] = '_';
            printPermutations(s, ans+currChar);
            s[i] = currChar; // backtrack
        }
    }
}

int main(){
    printPermutations("abcd", "");
    return 0;
}