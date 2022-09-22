#include <bits/stdc++.h>
using namespace std;

bool check(TreeNode* root, long long mn, long long mx){
    if(!root) return true;
    if(root->val <= mn || root->val >= mx) return false;
    
    bool left = check(root->left, mn, root->val);
    bool right = check(root->right, root->val, mx);
    return left && right;
}

bool isValidBST(TreeNode* root) {
    return check(root, (long long)INT_MIN-1, (long long)INT_MAX+1);
}