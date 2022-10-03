#include <bits/stdc++.h>
using namespace std;

void subseq(string s, string ans, int i){
    if(i == s.length()){
        cout << ans << endl;
        return;
    }

    // to include current element
    subseq(s, ans, i + 1);
    subseq(s, ans + s[i], i + 1);
}

int main (){
    subseq("abc", "", 0);
    return 0;
}