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
        //DFS with recursion
        void preorder(Node *root){
            if(root == NULL) return;
            cout<<root->data<<" ";
            preorder(root->left);
            preorder(root->right);
        }

        void preorder_iterative(Node *root){
            if(!root) return;
            stack<Node*> s;
            s.push(root);
            while(!s.empty()){
                Node *currNode = s.top();
                cout<<currNode->data<<" ";
                s.pop();
                if(currNode->right) s.push(currNode->right);
                if(currNode->left) s.push(currNode->left);
            }
        }

        void inorder(Node *root){
            if(root == NULL) return;
            inorder(root->left);
            cout<<root->data<<" ";
            inorder(root->right);
        }

        void inorder_iterative(Node *root){
            if(!root) return;
            stack<Node*> s;
            s.push(root);

            unordered_map<Node*, int> cnt;
            while(!s.empty()){
                Node *curr = s.top();
                if(!curr) {s.pop(); continue;}
                if(cnt[curr] == 0) s.push(curr->left); // node visited first time.. visit left child first
                else if(cnt[curr] == 1) cout<<curr->data<<" "; // node's left child visited earlier
                else if(cnt[curr] == 2) s.push(curr->right); // node printed, now visit right child
                else s.pop(); // lowest subtree fully visited.. delete the subroot
                cnt[curr]++;
            }
        }

        void postorder(Node *root){
            if(root == NULL) return;
            postorder(root->left);
            postorder(root->right);
            cout<<root->data<<" ";
        }

        void postorder_iterative(Node *root){
            if(!root) return;
            stack<pair<Node*,int>> s;

            s.push({root, 0});
            while(!s.empty()){
                pair<Node*, int> p = s.top();
                Node* curr = p.first;
                int state = p.second;
                s.pop();
                if(!curr || state == 3) continue; // if empty node, dont push it back, ignore and continue
                s.push({curr, state+1}); // we are popping and pushing as editing inplace in stack is not possible
                if(state == 0) s.push({curr->left, 0}); // if node visited first time, visit left child first
                if(state == 1) s.push({curr->right, 0}); // if node visited second time, visit right child first
                if(state == 2){ 
                    cout<<curr->data<<" "; // finally after visiting all children, print the node and pop it from the stack
                    s.pop();
                }
            }
        }

        // BFS with iteration
        void levelOrder(Node *root){
            if(!root) return;
            queue<Node*> q;
            q.push(root);

            while(!q.empty()){
                Node *currNode = q.front();
                q.pop();
                cout<<currNode->data<<" ";
                if(currNode->left) q.push(currNode->left);
                if(currNode->right) q.push(currNode->right);
            }
        }

        // print levels
        void printLevels(Node* root){
            if(!root) return;
            queue<Node*> q;
            q.push(root);

            while(q.size()){
                int s = q.size();
                while(s--){
                    auto node = q.front();
                    cout << node->data << " ";
                    
                    if(s == 0) cout << "\n"; // level end

                    if(node->left) q.push(node->left);
                    if(node->right) q.push(node->right);
                }
            }
        }

        // print levels - different approach using array
        void printLevels2(Node* root){
            if(!root) return;
            queue<Node*> q;
            q.push(root);
            vector<Node*> level;
            auto end = root;
            while(q.size()){
                auto node = q.front();
                level.push_back(node);
                if(node->left) q.push(node->left);
                if(node->right) q.push(node->right);

                if(node == end){
                    for(auto p : level) cout << p->data << " ";
                    cout << endl;
                    end = q.back();
                    level.clear();
                }
            }
        }

        // count number of nodes in a tree
        int countNodes(Node *root){
            return root ? 1 + countNodes(root->left) + countNodes(root->right) : 0;
        }

        // calculate height of a tree
        int treeHeight(Node *root){
            return root ? 1 + max(treeHeight(root->left), treeHeight(root->right)) : 0;
        }

        // calculate the diameter of a tree(longest path in a tree)
        int treeDiameter(Node *root){
            return root ? max({treeDiameter(root->left), treeDiameter(root->right), 1 + treeHeight(root->left) + treeHeight(root->right)}) : 0;
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
    tree.preorder(root); // prints preorder sequence of the tree:- 1 2 3 4 5 6
    cout<<endl;
    tree.preorder_iterative(root); // prints preorder sequence of the tree:- 1 2 3 4 5 6
    cout<<endl;
    tree.inorder(root); // prints inorder sequence of the tree:- 4 2 5 1 3 6
    cout<<endl;
    tree.inorder_iterative(root); // prints inorder sequence of the tree:- 4 2 5 1 3 6
    cout<<endl;
    tree.postorder(root); // prints postorder sequence of the tree:- 4 5 2 6 3 1
    cout<<endl;
    tree.postorder_iterative(root); // prints postorder sequence of the tree:- 4 5 2 6 3 1
    cout<<endl;
    tree.levelOrder(root); // prints level order sequence of the tree:- 1 2 3 4 5 6
    cout<<endl;
    cout<<tree.countNodes(root); // prints number of nodes in the tree:- 6
    cout<<endl;
    cout<<tree.treeHeight(root); // prints height of the tree:- 3
    cout<<endl;
    cout<<tree.treeDiameter(root); // prints the diameter(longest path between two nodes) of the tree:- 5
}