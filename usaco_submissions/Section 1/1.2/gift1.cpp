#include <bits/stdc++.h>
using namespace std;

/*
TASK: gift1
USER: Vignesh Iyer
LANG: C++
*/

void read_input(string filename){
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

void solve(){
	int n; cin >> n;
	unordered_map<string, int> balance;
	string accounts[n];
	for(int i = 0; i < n; i++){
		string name;
		cin >> name;
		balance[name] = 0;
		accounts[i] = name;
	}
	
	string giver;
	for(int i = 0; i < n; i++){
	  cin >> giver;
		int amount, receivers;
		cin >> amount >> receivers;
		for(int k = 0; k < receivers; k++){
			string receiver;
			cin >> receiver;
			balance[giver] -= amount/receivers;
			balance[receiver] += amount/receivers;
		}
	}
	
	for(int i = 0; i < n; i++)
		cout << accounts[i] << " " << balance[accounts[i]] << "\n";
}

int main(){
	read_input("gift1");
	
	solve();
	return 0;
}