#include <bits/stdc++.h>
using namespace std;

struct point {
    int x, y;

    /* Comparison is done on y coordinate and then x */
    bool operator < (point &a) {
        if(y != a.y) return y < a.y;
        return x < a.x;
    }

    bool operator == (point &a) {
        return (a.x == x && a.y == y);
    }
};

point pivot;

/* if a,b,c are 3 pts then condition for clockwise angle is 
    (b.x-a.x)/(b.y-a.y) > (c.x-b.x)/(c.y-b.y) */
int dir(point a, point b, point c){
    int area = a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y);

    if(area > 0) return -1;  // counter clockwise
    else if(area < 0) return 1; // clockwise
    return 0; // colinear
}

int dist(point a, point b){
    int dx = a.x - b.x, dy = a.y - b.y;
    return dx*dx + dy*dy;
}

bool POLAR_ORDER(point a, point b){
    int order = dir(pivot, a, b);
    if(order == 0)
        return dist(pivot,a) < dist(pivot, b); 
    /* Sorting according to ccw angle */
    return order == -1;                             
}

stack<point> convex_hull(vector<point> &p){
    stack<point> hull;
    int n = p.size();

    /* Find the point having the least y (pivot) */
    int leastY = 0;
    for(int i = 1; i < n; i++) 
        if(p[i] < p[leastY]) leastY = i;

    /* swap the pivot and the first point */
    swap(p[leastY], p[0]);

    /* sort the remaining points according to the angle they make with the pivot */
    pivot = p[0];
    sort(p.begin() + 1, p.end(), POLAR_ORDER);

    hull.push(p[0]);
    hull.push(p[1]);

    for(int i = 2; i < n; i++){
        point top = hull.top(); hull.pop();
        point next = p[i];

        while(hull.size() && dir(hull.top(), top, next) > 0){
            top = hull.top();
            hull.pop();         /* Delete elements to create a ccw turn */
        }

        hull.push(top);
        hull.push(p[i]);
    }
    return hull;
}

vector<vector<int>> outerTrees(vector<vector<int>>& trees) {
    int n = trees.size();
    if(n < 3) return trees;
    
    vector<point> p;
    
    for(auto tree : trees) p.push_back({tree[0], tree[1]});
    
    vector<vector<int>> fences;
    auto hull = convex_hull(p);
    
    while(hull.size()){
        point t = hull.top(); hull.pop();
        fences.push_back({t.x, t.y});
    }
    return fences;
}

int main(){
    vector<vector<int>> trees = {{1,1},{2,2},{2,0},{2,4},{3,3},{4,2}};
    auto ans = outerTrees(trees);

    for(auto p : ans) cout << p[0] << " " << p[1] << endl;
    /*
    1 1
    2 4
    3 3
    4 2
    2 0
    */
}