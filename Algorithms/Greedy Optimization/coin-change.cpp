#include <bits/stdc++.h>
using namespace std;

/*
we consider a problem where we are given a set of coins and
our task is to form a sum of money n using the coins. The values of the coins are
coins = {c1, c2,..., ck}, and each coin can be used as many times we want. What
is the minimum number of coins needed?
*/

int minCoins(vector<int> coins, int amount){
    int count = 0;
    int hi = coins.size()-1;
    while(amount > 0){
        if((amount - coins[hi]) < 0) hi--;
        amount -= coins[hi];
        count++;
    }
    return count;
}

int main(){
    vector<int> coins = {1,2,5,10,20,50,100,200};
    int amount = 520;
    cout<<minCoins(coins, amount); // 4:- 200 + 200 + 100 + 20
    return 0;
}

/*
A simple greedy approach always selects the largest possible coin to reach the desired sum as quickly as possible.
This approach may work for certain set of examples. But for a given set of coins {1,3,4} and a target sum of 6 as a counterexample,
the algorithm fails to produce the optimal answer. 

expected output: 3 + 3 (2 coins)
actual output: 4 + 1 + 1 (3 coins)
*/