// Creates binary tree given the preorder sequence
#include <bits/stdc++.h>
#include <iostream>
using namespace std;

struct Node{
    int data;
    Node *left;
    Node *right;
};

// Idea is, we choose the first element of the array as our root, and then find the elements which are smaller than the root and the elements which are greater than the root.
// As this is a BST, all the smaller elements will be a part of the left subtree. Similarly the greater elements will be a part of the right subtree.
// We recursively solve for both the left and right subtree.
Node* BSTfromPreorder(vector<int>& arr){
    if(arr.empty()) return NULL;

    vector<int> smaller, greater;
    for(auto n : arr)
        if(n != arr[0]) (n < arr[0] ? smaller.push_back(n) : greater.push_back(n));

    Node* root = new Node();
    root->data = arr[0];
    root->left = BSTfromPreorder(smaller);
    root->right = BSTfromPreorder(greater);
    return root;
}

/* The above approach may be very slow given a tree which is skewed to the either side.
for eg. 
        1
         \
          2
           \
            3...  for every node, we will make n-1, parses.

            Therefore the time complexity is O(n^2)
*/

// Optimized approach O(n) time O(1) space
// Notice that in the array, [8,5,1,7,10,12] -> the only elements that can be in the left subtree are the ones smaller than the root.
// therefore instead of passing the whole array, we can just pass the limit value.
Node* BSTfromPreorder_v2(vector<int>& arr, int& id, int limit){
    if(arr[id] > limit || id == (int) arr.size()) return NULL;

    Node* root = new Node();
    root->data = arr[id++];
    root->left = BSTfromPreorder_v2(arr, id, root->data);
    root->right = BSTfromPreorder_v2(arr, id, limit);
    return root;
}

void inorder(Node* root){
    if(!root) return;
    inorder(root->left);
    cout << root->data << " ";
    inorder(root->right);
}

int main(){
    vector<int> arr = {8,5,1,7,10,12};
    int id = 0;
    auto root = BSTfromPreorder_v2(arr, id, INT_MAX);

    inorder(root); // 1 5 7 8 10 12
}