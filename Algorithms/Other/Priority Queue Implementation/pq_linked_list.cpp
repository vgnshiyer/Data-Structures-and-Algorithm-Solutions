#include <bits/stdc++.h>
using namespace std;

struct Node{
    int data;
    int priority;

    struct Node* next;
};

Node* newNode(int data, int priority){
    Node* head = new Node;
    head->data = data;
    head->priority = priority;
    head->next = NULL;
    return head;
}

int peek(Node *head){
    return head->data;
}

void pop(Node *head){
    auto temp = head;
    head = head->next;
    free(temp);
}

void push(Node *head, int data, int priority){
    Node* temp = newNode(data, priority);
    if(head->priority < priority){
        temp->next = head;
        head = temp;
    } else{
        auto start = head;
        while(start->next != NULL && start->next->priority > priority){
            start = start->next;
        }
        temp->next = start->next;
        start->next = temp;
    }
}

bool isEmpty(Node *head){return head == NULL;}

int main(){
    Node *head = newNode(4,1);
    push(head, 5, 2);
    push(head, 6, 3);
    push(head, 7, 0);

    while(!isEmpty(head)){
        cout << " " << peek(head);
        pop(head);
    }
}