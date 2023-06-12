/* Disjoing set union : Union by rank_ */
#include<bits/stdc++.h>
using namespace std;

const int N = 1000;
int parent[N];
int rank_[N];
pair<int, pair<int, int>> edges[N];
int v, n;

class DisjoinSet {
    vector<int> parent, rank_, size;
public:
    DisjoinSet(int n) {
        parent.resize(n+1, 0);
        rank_.resize(n+1, 0);
        size.resize(n+1, 0);
        for(int i = 0; i < n; i++) parent[i] = i;
    }

    int find(int a) {
        if(a != parent[a]) parent[a] = find(parent[a]);
        return a;
    }

    void union_by_rank(int a, int b) {
        int parenta = find(a);
        int parentb = find(b);
        if(rank_[parenta] > rank_[parentb])
            parent[parentb] =  parenta;
        else if(rank_[parenta] < rank_[parentb])
            parent[parenta] = parentb;
        else{
            parent[parentb] = parenta;
            rank_[parenta]++;
        }
    }

    void union_by_size(int a, int b) {
        int parenta = find(a);
        int parentb = find(b);
        if(size[parenta] < size[parentb]){
            parent[parenta] = parentb;
            size[parentb] += size[parenta];
        } else {
            parent[parentb] = parenta;
            size[parenta] += size[parentb];
        }
    }
};

int main() {
    DisjoinSet ds(7);
    ds.union_by_rank(1,2);    
    ds.union_by_rank(2,3);    
    ds.union_by_rank(4,5);    
    ds.union_by_rank(5,6);    
    ds.union_by_rank(6,7);    
    ds.union_by_rank(3,7);    
}