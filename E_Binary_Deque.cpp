#include <bits/stdc++.h>
using namespace std;

#define fo(i,n) for(i=0;i<n;i++)
#define ll long long
#define si(x)	scanf("%d",&x)
#define sl(x)	scanf("%lld",&x)
#define ss(s)	scanf("%s",s)
#define pi(x)	printf("%d\n",x)
#define pl(x)	printf("%lld\n",x)
#define ps(s)	printf("%s\n",s)
#define pb push_back
#define sz(a)   (int)a.size()
#define mp make_pair
#define F first
#define S second
#define deb(x) cout << #x << "=" << x << endl
#define deb2(x, y) cout << #x << "=" << x << "," << #y << "=" << y << endl
#define all(x) x.begin(), x.end()
#define sortall(x) sort(all(x))
#define tr(it, a) for(auto it = a.begin(); it != a.end(); it++)
#define PI 3.1415926535897932384626
typedef pair<int, int>	pii;
typedef pair<ll, ll>	pl;
typedef vector<int>		vi;
typedef vector<ll>		vl;
typedef vector<pii>		vpii;
typedef vector<pl>		vpl;
typedef vector<vi>		vvi;
typedef vector<vl>		vvl;
const int N = 3e5;

int main() {
    int t, i, n, s;
    si(t);
    while(t--){
        cin >> n >> s;
        int a[n];
        fo(i, n) cin >> a[i];

        int lo = 0, hi = 0, currSum = 0, currLen = INT_MIN;
        while(lo < n && hi < n){
            currSum += a[hi];
            if(currSum == s) currLen = max(currLen, hi - lo + 1);
            if(currSum <= s) hi++;
            else{
                currSum -= (a[lo++]+a[hi]);
            }
        }
        cout <<(currLen == INT_MIN ? -1 : n-currLen)<<endl;
    }
    return 0;
}