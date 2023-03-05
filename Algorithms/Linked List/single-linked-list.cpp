#include<bits/stdc++.h>
using namespace std;

struct Node{
    int val;
    Node* next = NULL;
};

Node* insert_back(Node* head, int val){
    if(!head){
        Node* head = new Node();
        head->val = val;
        return head;
    }

    Node* temp = head;
    while(temp->next) temp = temp->next;

    Node* node = new Node();
    node->val = val;
    temp->next = node;
    return head;
}

Node* insert_front(Node* head, int val){
    Node* newNode = new Node();
    newNode->val = val;
    newNode->next = head;
    return newNode;
}

Node* insert_middle(Node* head, int val, int pos){
    if(pos == 1) return insert_front(head,val);

    Node* temp = head;
    while(pos-- > 1)
        temp = temp->next;

    Node* newNode = new Node();
    newNode->val = val;
    Node* next = temp->next;
    temp->next = newNode;
    newNode->next = next;
    return head;
}

Node* delete_first(Node* head){
    return head->next;
}

Node* delete_last(Node* head){
    Node* temp = head;
    while(temp->next->next) temp = temp->next;
    temp->next = NULL;
    return head;
}

Node* delete_middle(Node* head, int pos){
    if(pos == 1) return delete_first(head);

    Node* temp = head;
    while(pos-- > 1)
        temp = temp->next;
    if(temp->next == NULL){
        cout << "Invalid input!!";
        return head;
    }
    temp->next = temp->next->next;
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
    Node* head = NULL;
    head = insert_back(head, 1);
    head = insert_back(head, 2);
    head = insert_back(head, 3);
    head = insert_back(head, 4);

    print_list(head);

    head = insert_front(head, 0);
    head = insert_front(head, -1);

    print_list(head);

    head = insert_middle(head, 3,4);

    print_list(head);

    head = delete_first(head);

    print_list(head);

    head = delete_last(head);

    print_list(head);

    delete_middle(head, 2);

    print_list(head);
    return 0;
}