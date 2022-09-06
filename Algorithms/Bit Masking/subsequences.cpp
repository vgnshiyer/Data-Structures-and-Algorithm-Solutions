#include <bits/stdc++.h>
using namespace std;

void print_subseq(string S){
    int N = S.size();
    for(int mask = 0; mask < 1 << N; mask++){
        string seq;
        for(int j = 0; j < 3; j++){
            if(mask & 1 << j)
                seq += S[j];
        }
        cout << seq << "\n";
    }
}

int main(){
    print_subseq("ABC");
    return 0;
}