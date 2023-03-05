#include<bits/stdc++.h>
using namespace std;

struct Node{
    int val;
    Node* next = NULL;
    Node* prev = NULL;
};

Node* insert_back(Node* head, int val){
    Node* newNode = new Node();
    newNode->val = val;
    if(head == NULL){
        return newNode;
    }

    Node* temp = head;
    while(temp->next) temp = temp->next;

    temp->next = newNode;
    newNode->prev = temp;
    return head;
}

Node* insert_front(Node* head, int val){
    Node* newNode = new Node();
    newNode->val = val;

    if(head == NULL){
        return newNode;
    }

    newNode->next = head;
    head->prev = newNode;
    return newNode;
}

Node* insert_middle(Node* head, int val, int pos){
    Node* newNode = new Node();
    newNode->val = val;

    Node* temp = head;
    while(pos-- > 1) temp = temp->next;

    Node* next = temp->next;
    temp->next = newNode;
    newNode->prev = temp;
    newNode->next = next;
    return head;
}

void print_list(Node* head){
    Node* temp = head;
    while(temp){
        cout << temp->val << " ";
        temp = temp->next;
    }
    cout << endl;
}

int main(){
    Node* head = insert_back(NULL, 1);
    head = insert_back(head, 2);
    head = insert_back(head, 3);
    head = insert_front(head, 0);
    head = insert_front(head, -1);

    print_list(head);

    head = insert_middle(head, 3, 3);

    print_list(head);

    return 0;
}