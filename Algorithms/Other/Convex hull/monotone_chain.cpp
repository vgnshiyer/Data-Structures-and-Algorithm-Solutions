#include <bits/stdc++.h>
using namespace std;

struct point {
    int x, y;
    
    /* to sort points from left to right 
    points with same x coordinate will be sorted based on y coordinate */
    bool operator < (point &a){
        return x < a.x || (x == a.x && y < a.y);
    }
    
    bool operator == (point &a){
        return (a.x == x && a.y == y);
    }
};

/* cross product of two vectors
returns +ve val if abc make a ccw turn 
returns -ve val if abc make a cw turn
return 0 if they are coliniear */
int dir(point a, point b, point c){
    return a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y);
}

/* Returns list of points on the convex hull in counter clockwise order */
vector<point> convex_hull(vector<point> p){
    /* Sort points lexicographically */
    sort(p.begin(), p.end());
    int n = p.size();
    
    vector<point> hull;
    
    /* Build lower hull */
    for(int i = 0; i < n; i++){
        while(hull.size() >= 2 && dir(hull[hull.size() - 2], hull.back(), p[i]) < 0){
            hull.pop_back();
        }
        hull.push_back(p[i]);
    }
    hull.pop_back();
    
    /* Build upper hull */
    for(int i = n-1; i >= 0; i--){
        while(hull.size() >= 2 && dir(hull[hull.size() - 2], hull.back(), p[i]) < 0){
            hull.pop_back();
        }
        hull.push_back(p[i]);
    }
    hull.pop_back();
    sort(hull.begin(), hull.end());
    hull.erase(unique(hull.begin(), hull.end()), hull.end());
    return hull;
}

vector<vector<int>> outerTrees(vector<vector<int>>& trees) {
    int n = trees.size();
    if(n <= 3) return trees;
    
    vector<point> p;
    for(auto t : trees) p.push_back({t[0], t[1]});
    
    auto hull = convex_hull(p);
    vector<vector<int>> answer;
    for(auto pt : hull) answer.push_back({pt.x, pt.y});
    
    return answer;
}

int main(){
    vector<vector<int>> trees = {{1,1},{2,2},{2,0},{2,4},{3,3},{4,2}};
    auto ans = outerTrees(trees);

    for(auto p : ans) cout << p[0] << " " << p[1] << endl;
    /*
    1 1
    2 0
    2 4
    3 3
    4 2
    */
}