#include <bits/stdc++.h>
using namespace std;

/*
TASK: transform
USER: Vignesh Iyer
LANG: C++
*/

int n; 
vector<vector<char>> before;
vector<vector<char>> after;

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

void reflect(){
    for(int i = 0; i < n; i++)
    for(int j = 0; j < n/2; j++){
        swap(before[i][j], before[i][n-1-j]);
    }
}

bool check(int choice){
    switch (choice)
    {
    case 1:
        /* 90 degree rotation */
        for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++){
            if(after[i][j] != before[n-1-j][i]) return false;
        }
        return true;
    
    case 2:
        /* 180 degree rotation */
        for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++){
            if(after[i][j] != before[n-1-i][n-1-j]) return false;
        }
        return true;
        
    case 3:
        /* 270 degree rotation */
        for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++){
            if(after[i][j] != before[j][n-1-i]) return false;
        }
        return true;

    case 4:
        /* reflection */
        for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++){
            if(after[i][j] != before[i][n-1-j]) return false;
        }
        return true;

    case 5:
        /* Combination */
        reflect();
        if(check(1) || check(2) || check(3)) return true;
        reflect();
        return false;

    case 6:
        /* No Change */
        for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++){
            if(before[i][j] != after[i][j]) return false;
        }

    default:
        return true;
    }
}

void solve(){
    cin >> n;
    before.resize(n,vector<char>(n));
    after.resize(n,vector<char>(n));

    for(int i = 0; i < n; i++){
        string a; cin >> a;
        for(int j = 0; j < n; j++)
            before[i][j] = a[j];
    }

    for(int i = 0; i < n; i++){
        string a; cin >> a;
        for(int j = 0; j < n; j++)
            after[i][j] = a[j];
    }

    for(int choice = 1; choice <= 7; choice++){
        if(check(choice)){
            cout << choice << "\n";
            break;
        }
    }
}

int main() {
    read_input("transform");
    int tc = 1;
    // cin >> tc;
    while(tc--)
        solve();

    return 0;
}