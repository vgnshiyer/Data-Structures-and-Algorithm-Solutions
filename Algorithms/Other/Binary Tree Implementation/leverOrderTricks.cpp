// Creates binary tree given the preorder sequence
#include <bits/stdc++.h>
#include <iostream>
using namespace std;

struct Node{
    int data;
    Node *left;
    Node *right;
};

class binaryTree{
    public:
        Node* createNode(int data){
            Node *node = new Node();
            node->data = data;
            node->left = NULL;
            node->right = NULL;
            return node;
        }

        int idx = -1;
        Node* buildTree(int nodes[]){
            idx++;
            if(nodes[idx] == -1) return NULL;

            Node *root = createNode(nodes[idx]);
            //create left subtree
            root->left = buildTree(nodes);
            //create right subtree
            root->right = buildTree(nodes);

            return root;
        }

    vector<vector<int>> levelOrder(Node* root) {
        if(!root) return {};
        
        queue<Node*> q;
        q.push(root);
        auto level_end = root;
        vector<int> level;
        vector<vector<int>> levels;
        
        while(!q.empty()){
            auto node = q.front();
            q.pop();
            level.push_back(node->data);
            
            if(node->left) q.push(node->left);
            if(node->right) q.push(node->right);
            
            if(level_end == node){
                levels.push_back(level);
                level.clear();
                level_end = q.back();
            }
        }
        return levels;
    }
};

int main(){
    int nodes[] = {1, 2, 4, -1, -1, 5, -1, -1, 3, -1, 6, -1, -1};
    binaryTree tree;
    Node *root = tree.buildTree(nodes);
    /*
    creates below binary tree and returns the root
                 1
                / \
              2    3
             / \    \
            4   5    6
    */
    
    auto levels = tree.levelOrder(root);
    // for(auto level : levels){
    //     for(int i = 0; i < level.size(); i++){
    //         cout << level[i] << " \n"[i == level.size()-1];
    //     }
    // }

    cout << "Left view of a tree \n";
    for(auto level : levels)
        cout << level[0] << " ";
    cout << endl;

    cout << "Right view of a tree \n";
    for(auto level : levels)
        cout << level[level.size() - 1]  << " ";

    // Left view of a tree 
    // 1 2 4 
    // Right view of a tree 
    // 1 3 6 
}