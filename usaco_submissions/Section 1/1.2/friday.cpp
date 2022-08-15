#include <bits/stdc++.h>
using namespace std;

/*
TASK: friday
USER: Vignesh Iyer
LANG: C++
*/

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

int days[7];
int days_in_a_month[12] = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };;


bool is_leap(int y){
	return (y%400 == 0) || (y%100 != 0 && y%4 == 0);
}

void solve(){
	int n; cin >> n;
	int curr = 0; // 13th january 1900 was a saturday
	for(int y=1900; y<1900+n; y++){
		// count 13th of every month
		for(int m = 0; m < 12; m++){
		  days[curr]++;
			curr += days_in_a_month[m];
			if(m == 1 && is_leap(y)) curr++;
			curr %= 7;
		}
	}
	
	for(int i = 0; i < 7; i++){
		cout << days[i];
		if(i < 6) cout << " ";
	}
	cout << "\n";
}

int main(){
	read_input("friday");
	
	solve();
	return 0;
}