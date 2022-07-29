#include <bits/stdc++.h>
using namespace std;

/*
TASK: palsquare
USER: Vignesh Iyer
LANG: C++
*/

// n = 6
// i = 2, j = 3
// abaaaba

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

bool is_palindrome(string s){
    int n = s.size();
    int i = n/2 - 1, j = (n+1)/2;
    for(; i>=0 && j<n; i--,j++){
        if(s[i] != s[j]) return false;
    }
    return true;
}

char hm[] = {'A','B','C','D','E','F','G','H','I','J','K'};

string convert(int n, int b){
    string ans;
    while(n){
        int rem = n%b;
        if(rem >= 10)
           ans = hm[rem - 10] + ans;
        else
            ans = to_string(rem) + ans;
        n /= b;
    }
    return ans;
}

void solve(){
    int b; cin >> b;
    for(int i = 1; i <= 300; i++){
        string num_in_b = convert(i, b);
        string sq_in_b = convert(i*i, b);
        if(is_palindrome(sq_in_b))
            cout << num_in_b << " " << sq_in_b << "\n";   
    }
}

int main() {
    read_input("palsquare");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}