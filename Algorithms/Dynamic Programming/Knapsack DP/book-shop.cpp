/*
You are in a book shop which sells n different books. You know the price and number of pages of each book.

You have decided that the total price of your purchases will be at most x. What is the maximum number of pages you can buy? You can buy each book at most once.

4 10
price: {4 8 5 3}
pages: {5 12 8 1}
*/

#include<bits/stdc++.h>
using namespace std;

int n, x;
vector<int> price, pages;
vector<vector<int>> dp;

int max_pages_iterative(){
    vector<vector<int>> dp(n+1, vector<int>(x+1, 0));
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= x; j++){
            dp[i][j] = dp[i-1][j]; // we either buy the current book or we skip it. depends on which choice gives us the maximum number of pages.
            if(price[i-1] <= j)
                dp[i][j] = max(pages[i-1] + dp[i-1][j-price[i-1]], dp[i][j]);
        }
    }

    return dp[n][x];
}

int max_pages_recursive(int i, int j){
    if(j > x) return 0;
    if(i >= n) return 0;
    
    int &ans = dp[i][j];
    if(ans != -1) return ans;
    
    // include the current book
    int include = INT_MIN;
    if(j + price[i] <= x)
        include = pages[i] + max_pages_recursive(i + 1, j + price[i]);
    
    // exclude the current book
    int exclude = max_pages_recursive(i + 1, j);
    
    return ans = max(exclude, include);
}

int main(){
    price.resize(n);
    pages.resize(n);
    for(int i = 0; i < n; i++) cin >> price[i];
    for(int i = 0; i < n; i++) cin >> pages[i];

    dp.resize(n+1, vector<int>(x+1, -1));

    cout << max_pages_iterative() << endl;
    cout << max_pages_recursive(0, 0) << endl;
}