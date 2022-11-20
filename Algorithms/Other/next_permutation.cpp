#include <bits/stdc++.h>
using namespace std;
/*
    Generation in lexicographic order Algorithm
    The following algorithm generates the next permutation lexicographically after a given permutation. It changes the given permutation in-place.

    * Find the largest index i such that a[i] < a[i + 1]. If no such index exists, the permutation is the last permutation.
    * Find the largest index k greater than i such that a[i] < a[k].
    * Swap the value of a[i] with that of a[k].
    * Reverse the sequence from a[i + 1] up to and including the final element a[n].    
*/
bool nextPermutation(vector<int>& nums) {
    int i = nums.size()-1;
    if(i == 0) return false;
    while(true){
        int j = i;
        i--;
        
        if(nums[i]<nums[j]){
            int k = nums.size()-1;
            
            while(nums[i] >= nums[k]) k--;
            swap(nums[i], nums[k]);
            reverse(nums.begin()+j, nums.end());
            return true;
        }
        if(i == 0){
            reverse(nums.begin(), nums.end());
            return false;
        }
    }
}

// Actual c++ implementation of next_permutation inbuilt function
bool next_permutation(It begin, It end)
{
    if (begin == end)
            return false;

    It i = begin;
    ++i;
    if (i == end)
            return false;

    i = end;
    --i;

    while (true)
    {
            It j = i;
            --i;

            if (*i < *j)
            {
                    It k = end;

                    while (!(*i < *--k))
                            ;

                    iter_swap(i, k);
                    reverse(j, end);
                    return true;
            }

            if (i == begin)
            {
                    reverse(begin, end);
                    return false;
            }
    }
}

int main(){
    vector<int> nums;
    nextPermutation(nums);
    return 0;
}