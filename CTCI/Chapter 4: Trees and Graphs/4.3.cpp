#include<bits/stdc++.h>
using namespace std;

struct Node {
    Node* left = NULL;
    Node* right = NULL;
    int data = 0;
};

Node* buildTree(vector<int> nodes, int i) {
    if(i >= nodes.size()) return NULL;

    Node* root = new Node();
    root->data = nodes[i];
    int left = 2*i + 1;
    int right = 2*i + 2;
    root->left = buildTree(nodes, left);
    root->right = buildTree(nodes, right);
    return root;
}

void getLevels(Node* root, vector<vector<int>>& levels, int level) {
    if(!root){
        return;
    }

    if(levels.size() == level){
        // create new level array
        vector<int> currentLevel;
        levels.push_back(currentLevel);
    }
    vector<int>& currentLevel = levels[level];

    currentLevel.push_back(root->data);
    getLevels(root->left, levels, level + 1);
    getLevels(root->right, levels, level + 1);
}

vector<vector<int>> getLevelsBFS(Node* root){
    vector<vector<int>> levels;

    queue<Node*> q;
    q.push(root);

    while(!q.empty()) {
        int n = q.size();
        vector<int> level;
        while(n--){
            Node* cur = q.front();
            level.push_back(cur->data);
            q.pop();

            if(cur->left) q.push(cur->left);
            if(cur->right) q.push(cur->right);
        }
        levels.push_back(level);
    }
    return levels;
}

void displayLevels(vector<vector<int>> levels){
    for(auto level : levels) {
        for(int node : level){
            cout << node << " -> ";
        }
        cout << endl;
    }
}

int main() {
    Node* root = buildTree({1,2,3,4,5,6,7}, 0);

    vector<vector<int>> levels = {};
    getLevels(root, levels, 0);

    displayLevels(levels);
    /*
        1 -> 
        2 -> 3 -> 
        4 -> 5 -> 6 -> 7 -> 
    */
    auto levels2 = getLevelsBFS(root);
    displayLevels(levels2);
    /*
        1 -> 
        2 -> 3 -> 
        4 -> 5 -> 6 -> 7 ->
    */
    return 0;
}