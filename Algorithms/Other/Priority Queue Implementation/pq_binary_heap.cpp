#include <bits/stdc++.h>
using namespace std;

int H[50];
int size = -1;

int parent(int i){ return (i-1)/2;}
int leftChild(int i){ return 2*i + 1;}
int rightChild(int i){ return 2*i + 2;}

void percolate_up(int i){
    while(i > 0 && H[parent(i)] < H[i]){
        swap(H[parent(i)], H[i]);
        i = parent(i);
    }
}

void percolate_down(int i){
    int maxidx = i;

    int l = leftChild(i);

    if(l <= size && H[l] > H[maxidx]){
        maxidx = l;
    }

    int r = rightChild(i);

    if(r <= size && H[r] > H[maxidx]){
        maxidx = r;
    }

    if(i != maxidx){
        swap(H[i], H[maxidx]);
        percolate_down(maxidx);
    }
}

void insert(int p){
    size++;
    H[size] = p;

    percolate_up(size);
}

int pop(){
    int result = H[0]; // root is largest
    
    H[0] = H[size];
    size--;

    percolate_down(0);
    return result;
}

int peek(){
    return H[0];
}

int main(){
    /*         45
            /      \
           31      14
          /  \    /  \
         13  20  7   11
        /  \
       12   7
    Create a priority queue shown in
    example in a binary max heap form.
    Queue will be represented in the
    form of array as:
    45 31 14 13 20 7 11 12 7 */
 
    // Insert the element to the
    // priority queue
    insert(45);
    insert(20);
    insert(14);
    insert(12);
    insert(31);
    insert(7);
    insert(11);
    insert(13);
    insert(7);

    for(int i = 0; i <= size; i++)
        cout << H[i] << " ";

    cout << "\n";

    cout << peek() << "\n";
    cout << pop() << "\n";

    for(int i = 0; i <= size; i++)
        cout << H[i] << " ";

    return 0;
}