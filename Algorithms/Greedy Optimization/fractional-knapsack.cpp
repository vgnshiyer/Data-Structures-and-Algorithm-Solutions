#include <bits/stdc++.h>
using namespace std;

/*
Given the weights and values of n items, 
we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
*/

bool compare_ratio(pair<int,int> a, pair<int,int> b){
    return (double)a.first/a.second > (double)b.first/b.second;
}

int knapsack_sum(vector<pair<int,int>> knapsack, int capacity){
    // sorting the elements in the bag in the profit to weight ratio
    sort(knapsack.begin(),knapsack.end(), compare_ratio);

    int total_weight = 0, total_profit = 0;
    int i = 0;
    while(total_weight < capacity){
        if(knapsack[i].second <= capacity-total_weight){
            total_weight += knapsack[i].second;
            total_profit += knapsack[i].first;
        } else{
            double fraction = (double)capacity*(double)(capacity - total_weight)/knapsack[i].second;
            total_weight = capacity;
            total_profit += fraction*knapsack[i].first;
        }
        i++;
    }
    return total_profit;
}