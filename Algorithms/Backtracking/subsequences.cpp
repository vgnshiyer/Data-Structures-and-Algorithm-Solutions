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

void subseq2(string s, string ans){
    cout << ans << endl;
    for(int i = 0; i < s.length(); i++)
        subseq2(s.substr(i+1, s.length()), ans + s[i]);
}

int main (){
    subseq("abc", "", 0);
    cout << "\nCompact Version : " << endl;
    subseq2("abc", "");
    return 0;
}