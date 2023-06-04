#include<bits/stdc++.h>
using namespace std;

struct TreeNode {
    long long val;
    TreeNode* left;
    TreeNode* right;
};

class Solution {
public:
    unordered_map<long long, int> hashSet;
    int ans = 0;

    void checkPath(TreeNode* root, long long runningSum, int targetSum) {
        if(!root) return;

        runningSum += root->val;
        if(runningSum == targetSum) ans++;
        ans += hashSet[runningSum - targetSum];

        hashSet[runningSum]++;
        checkPath(root->left, runningSum, targetSum);
        checkPath(root->right, runningSum, targetSum);
        hashSet[runningSum]--;
    }

    int pathSum(TreeNode* root, int targetSum) {
        checkPath(root, 0, targetSum);
        return ans;
    }
};