#include <bits/stdc++.h>
using namespace std;

class LRUCache {
    int capacity;
    list<int> lru;
    unordered_map<int, list<int>::iterator> cache;
    unordered_map<int, int> kv;
public:
    LRUCache(int size){
        capacity = size;
    }

    int get(int key){
        if(kv.count(key) == 0) return -1;
        updateLRU(key);
        return kv[key];
    }

    int put(int key){
        // insert key val pair in to the cache
        // if cache is full, use LRU policy to evict an element from the cache
        if(kv.size() == capacity && kv.count(key) == 0)
            evict();
        updateLRU(key);
        kv[key] = value;
    }

    void updateLRU(int key){
        if(kv.count(key))
            lru.erase(cache[key]);
        lru.push_back(key);
        auto it = lru.end();
        it--;
        cache[key] = it;
    }

    void evict(){
        cache.erase(lru.front());
        kv.erase(lru.front());
        lru.pop_front();
    }
};