#include <bits/stdc++.h>

using namespace std;

int a[5] = {600, 60, 0, 10, 1};
int good[16] = {0, 70, 140, 210, 280, 350, 601, 671, 741, 811, 881, 951, 1202, 1272, 1342, 1412};

void solve() {
	string s;
	cin >> s;
	int x;
	cin >> x;
	int tot = 0;
	for (int i = 0; i < 5; i++) {
		tot += (int)(s[i] - '0') * a[i];
	}
	set<int> t;
	for (int i = 0; i < 2022; i++) {
		t.insert(tot);
		tot += x;
		tot %= 1440;
	}
	int res = 0;
	for (int i : t) {
		for (int j = 0; j < 16; j++) {
			if (good[j] == i) {res++;}
		}
	}
	cout << res << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int tt; cin >> tt; for (int i = 1; i <= tt; i++) {solve();}
    // solve();
}