#include <bits/stdc++.h>
using namespace std;

struct trie {
    trie *refs[26];
    bool isEnd = false;

    bool isContainsKey(char c){
        return (refs[c - 'a'] != NULL);
    }

    void put(char c, trie* node){
        refs[c - 'a'] = node;
    }

    trie* get(char c){
        return refs[c - 'a'];
    }

    void end(){
        isEnd = true;
    }
};

void insert(string word, trie* node){
    for(char c : word){
        if(!node->isContainsKey(c))
            node->put(c, new trie());
        node = node->get(c);
    }
    node->end();
}

bool search(string word, trie* root){
    trie* node = root;
    for(char c : word){
        if(!node->isContainsKey(c)) return false;
        node = node->get(c);
    }
    return node->isEnd;
}

bool startsWith(string prefix, trie* root){
    trie* node = root;
    for(char c : prefix){
        if(!node->isContainsKey(c)) return false;
        node = node->get(c);
    }
    return true;
}

int main(){
    trie* root = new trie();

    insert("apple", root);
    insert("cow", root);
    insert("bat", root);
    insert("app", root);

    cout << (search("apple", root) ? "present" : "absent") << endl;
    cout << (search("appl", root) ? "present" : "absent") << endl;
    cout << (startsWith("appl", root) ? "present" : "absent") << endl;

    /* OUTPUT: 
        present
        absent
        present    
    */

    return 0;
}