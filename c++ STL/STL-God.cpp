#include <bits/stdc++.h>
using namespace std;

bool func(int x, int y){ return x > y;}

void vector_demo(){
    vector<int> A = {1, 3, 14, 2, 5};

    cout<<A[1]<<endl; // 3

    sort(A.begin(), A.end()); // O(nlogn)
    // 1 2 3 5 14

    bool present = binary_search(A.begin(), A.end(), 3); // true // O(logn)
    present = binary_search(A.begin(), A.end(), 15); // false

    A.push_back(100);
    A.push_back(100);
    A.push_back(100);
    A.push_back(123);
    // 1 2 3 5 14 100 100 100 123

    vector<int>::iterator it = lower_bound(A.begin(), A.end(), 100); // least number >= 100 -- ans 5 // O(logn)
    auto it2 = upper_bound(A.begin(), A.end(), 100); // least number > 100 -- ans 8 // O(logn)
    
    cout<<*it<<" "<<*it2<<endl; // 100 123 
    cout<<it2 - it<<endl; // 3 (number of times 100 occurs in the vector) // o(1)

    sort(A.begin(),A.end(),func);
    for(vector<int>::iterator it3 = A.begin(); it3 != A.end(); it3++){
        cout<<*it3<<" ";
    }
    cout<<endl;

    for(auto x : A) cout<<x<<" ";
    cout<<endl;

    // changing values by reference
    for(auto &x : A) x++;
    for(auto x : A) cout<<x<<" ";
    cout<<endl;
}

void set_demo(){
    set<int> S; // uses a binary tree in the backend
    S.insert(1); // inserts in O(logn) time
    S.insert(2);
    S.insert(-1);
    S.insert(-2);
    // sets insert the elements in sorted order.. so we dont need to sort them explicitly-- saves time
    for(auto x : S) cout<<x<<" "; // -2 -1 1 2
    cout<<endl;

    auto it = S.find(-1);
    if(it == S.end()) cout<<"Not Present\n";
    else cout<<*it<<" is Present\n";

    auto it2 = S.upper_bound(-1); 
    cout<<*it2<<" \n";

    S.erase(-1); // removes in O(logn) time:- -2 1 2

    /*
    unordered_set also performs the same operations but with faster time complexity O(1)
    It uses hashing internally instead of binary trees as it does not maintain the order of elements.
    */
}

void map_demo(){
    map<int, int> M;
    M[1] = 100; // O(log n) time  insertion
    M[2] = 200;
    M[3] = 300;

    map<char, int> cnt;
    string s = "vignesh iyer";
    for(char c : s) cnt[c]++;

    cout<<"v = "<<cnt['v']<<" i = "<<cnt['i']<<endl;
}

void powerOfSTL(){
    set<pair<int, int>> S;
    S.insert({10,20});
    S.insert({30,100});
    S.insert({101,2000});
    S.insert({1,9});

    // this will be sorted in the order of the first elements of the pairs
    // if first elements are equal, then on the second elements.

    auto it = S.upper_bound({50, INT_MAX});
    if(it == S.begin()){
        cout<<"the point is not lying in any interval\n";
        return;
    }
    it--;
    auto current = *it;
    if(current.first <= 50 && current.second >= 50){
        cout<<"the point is lying in interval\n"<<current.first<<" "<<current.second<<"\n";
    }else{
        cout<<"the point is not lying in any interval\n";
        return;
    }

}

int main(){
    // vector_demo();
    // set_demo();
    // map_demo();
    powerOfSTL();
    return 0;
}