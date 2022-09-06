#include <bits/stdc++.h>
using namespace std;

void minimum_varied_number(int s){
    int ans = 1e9;

    for(int mask = 0; mask < 1 << 9; mask++){
        int sum = 0;
        string num;

        for(int i = 0; i < 9; i++){
            if(mask & 1 << i){ // check if ith bit is set?
                sum += i+1;
                num += char('0' + (i+1));
            }
        }
        if(sum != s) continue;
        ans = min(ans, stoi(num));
    }
    cout << ans << "\n";
}

int main(){
    minimum_varied_number(20);
    return 0;
}