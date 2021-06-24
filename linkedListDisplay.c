#include<stdio.h>
#include<stdlib.h>
struct Node{
    int data;
    struct Node* next;
} *first ;// global pointer or first implementation of said struct 


void create_link(int A[], int n){
    int i;
    struct Node *t, *last;
    first= (struct Node*)malloc(sizeof(struct Node));
    first-> data= 0;
    first-> next = NULL;
    last= first;

    for(i=1; i<n; i++){
            t= (struct Node*)malloc(sizeof(struct Node));
            t-> data= A[i];
            t-> next= NULL;
            last-> next= t;
            last= t;

    }
}
void display(struct Node *p){
    while(p!=NULL){
            printf("%d \n", p-> data);
            p= p->next; 
    }
}

int main(){
    int A[]= {3,5,7,10, 15};
    create_link(A, 5);
    display(first);
}
