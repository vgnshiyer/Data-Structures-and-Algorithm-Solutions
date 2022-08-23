#include <bits/stdc++.h>
using namespace std;

/*
TASK: preface
USER: Vignesh Iyer
LANG: C++
*/

#define ll long long
#define nline "\n"

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

int n;
int letters[26];

string number_preface(int num){
    int d[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    string c[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

    string roman;
    int i = 0;
    while(num){
        int t = num/d[i];
        string s;
        for(int k = 0; k < t; k++) s += c[i];
        roman += s;
        num %= d[i++];
    }
    return roman;
}

void solve(){
    cin >> n;
    for(int x = 0; x <= n; x++){
        string r = number_preface(x);
        for(char a : r) letters[a - 'A']++;
    }

    for(auto c : {'I', 'V', 'X', 'L', 'C', 'D', 'M'})
        if(letters[c - 'A'])
            cout << c << " " << letters[c - 'A'] << nline;
}

int main() {
    read_input("preface");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}