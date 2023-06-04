#include<bits/stdc++.h>
using namespace std;

struct Node {
    Node* left = NULL;
    Node* right = NULL;
    int data = 0;
};

Node* buildTree(vector<int> nodes, int i) {
    if(i >= nodes.size()) return NULL;

    if(nodes[i] == -1){
        return NULL;
    }
    Node* root = new Node();
    root->data = nodes[i];
    int left = 2*i + 1;
    int right = 2*i + 2;
    root->left = buildTree(nodes, left);
    root->right = buildTree(nodes, right);
    return root;
}

int isBalanced(Node* root, int& result){
    if(!root) return 0;

    int left = isBalanced(root->left, result);
    int right = isBalanced(root->right, result);
    int difference = abs(left - right);
    if(difference > 1) {
        result &= 0;
    } else {
        result &= 1;
    }
    return 1 + max(left, right);
}

int main() {
    Node* root = buildTree({1,2,3,4,5,6,7}, 0);
    int result = 1; // false
    isBalanced(root, result);
    cout << (result ? "balanced" : "not balanced") << endl;
    // balanced

    Node* root2 = buildTree({1,2,3,4,-1,-1,-1,5,-1}, 0);
    result = 1; // false
    isBalanced(root2, result);
    cout << (result ? "balanced" : "not balanced") << endl;
    // not balanced

    return 0;
}