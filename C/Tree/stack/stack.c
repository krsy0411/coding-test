#include <stdio.h>
#define SIZE 100

typedef struct TreeNode {
    int data;
    TreeNode* left;
    TreeNode* right;
} TreeNode;

// 스택 "노드" 구조체
typedef struct StackNode {
    TreeNode* data;
    StackNode* next;
} StackNode;

// "스택" 구조체
typedef struct Stack {
    StackNode* top;
} Stack;

Stack* createStack() {
    Stack* stack = (Stack*)malloc(sizeof(Stack));
    stack->top = NULL;
    return stack;
}

void push(Stack* stack, TreeNode* data) {
    StackNode* newNode = (StackNode*)malloc(sizeof(StackNode));
    newNode->data = data;
    newNode->next = stack->top;
    stack->top = newNode;
}

TreeNode* pop(Stack* stack) {
    if(stack->top == NULL) {
        return NULL;
    }

    StackNode* temp = stack->top;
    TreeNode* popped = temp->data;

    stack->top = stack->top->next;
    free(temp);
    return popped;
}