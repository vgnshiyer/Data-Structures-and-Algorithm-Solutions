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

        vector<Node*> TopView(Node* root){
            stack<pair<Node*, int>> stk;
            stk.push({root, 0});
            map<int, vector<Node*>> hm;

            while(!stk.empty()){
                auto p = stk.top();
                stk.pop();
                auto node = p.first;
                int dist = p.second;
                hm[dist].push_back(node);

                if(node->left) stk.push({node->left, dist-1});
                if(node->right) stk.push({node->right, dist+1});
            }

            vector<Node*> topNodes;
            for(auto p : hm)
                topNodes.push_back(p.second[0]);
            return topNodes;
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
    
    cout << "The tree looks something like this from the top\n";
    auto topNodes = tree.TopView(root);
    for(auto node : topNodes) cout << node->data << " ";
    //The tree looks something like this from the top
    // 4 2 1 3 6 

    // same way get the bottom nodes... last elements from the hashmap
}