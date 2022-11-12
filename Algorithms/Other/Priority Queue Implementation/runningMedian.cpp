#include <bits/stdc++.h>
using namespace std;

class MedianFinder {
    priority_queue<int> maxHeap;
    priority_queue<int, vector<int>, greater<int>> minHeap;
public: 
    MedianFinder(){
        /* Do nothing here */
    }

    void addNum(int num){
        maxHeap.push(num);   // add new num
        minHeap.push(maxHeap.top());   // push max from heap1 to heap2
        maxHeap.pop();

        if(minHeap.size() > maxHeap.size()){
            maxHeap.push(minHeap.top());
            minHeap.pop();
        }
    }

    double findMedian(){
        if(maxHeap.size() > minHeap.size()) return (double)maxHeap.top();
        return (maxHeap.top() + minHeap.top())/2.0;
    }
};

int main(){

    int arr[5] = {1, 2, 4, 3, 5};
    MedianFinder* medianFinder = new MedianFinder();
    for(int x : arr){
        medianFinder->addNum(x);
        cout << medianFinder->findMedian() << endl;
    }
    /*
    Output:
    1
    1.5
    2
    2.5
    3
    */
    return -1;
}