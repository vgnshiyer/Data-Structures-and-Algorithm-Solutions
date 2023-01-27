#include <bits/stdc++.h>
using namespace std;

/*
TASK: milk2
USER: Vignesh Iyer
LANG: C++
*/

#define nline "\n"
#define ll long long

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

struct milking {
    int s;
    int e;
};

int N;

void solve(){
    cin >> N;
    vector<milking> times;

    for(int i = 0; i < N; i++) {
        int s, e;
        cin >> s >> e;
        milking t;
        t.s = s, t.e = e;
        times.push_back(t);
    }

    sort(times.begin(), times.end(), [&](milking a, milking b){
        return a.s == b.s ? a.e <= b.e : a.s <= b.s;
    });
    
    auto prev = times[0];
    int t = prev.e - prev.s;
    int nomilk = 0, milk = t;
    for(int i = 1; i < N; i++){
        auto cur = times[i];
        if(cur.s > prev.e){
            int temp = times[i].s - prev.e;
            prev = times[i];
            nomilk = max(nomilk, temp);
        } else {
            if(cur.e > prev.e)
                prev.e = cur.e;
            milk = max(milk, prev.e - prev.s);
        }
    }
    cout << milk << " " << nomilk << nline;
}

int main(){
	read_input("milk2");
	
	solve();
	return 0;
}