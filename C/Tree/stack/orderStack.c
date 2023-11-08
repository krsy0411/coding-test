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

// 스택 - 전위 순회 : VLR
void stackPreorder(TreeNode* node) {
    TreeNode* stack[SIZE];
    int top = -1;
    push(stack, node);

    while(1) {
        node = pop(stack);
        if(node == NULL)
            break;
        printf("%d", node->data);

        // *** 오른쪽 자식노드를 먼저 push **
        if(node->right != NULL) {
            push(stack, node->right);
        }
        if(node->left != NULL) {
            push(stack, node->left);
        }
    }
}

// 스택 - 중위 순회 : LVR
void stackInorder(TreeNode* node) {
    TreeNode* stack[SIZE];
    int top = -1;
    while(1) {
        for(; node != NULL; node=node->left) {
            push(stack, node);
        }

        node = pop(stack);

        if(node == NULL)
            break;
        
        printf("%d ", node->data);
        node = node->right;
    }
}

// 스택 - 중위 순회 : LRV
void stackPostorder(TreeNode* node) {
    TreeNode* stack[SIZE];
    int print_stack[SIZE];
    int print_idx = -1;
    int top = -1;
    push(stack, node);
    while(1) {
        node = pop(stack);
        if(node == NULL)
            break;

        print_stack[++print_idx] = node->data;
        if(node->left != NULL) {
            push(stack, node->left);
        }
        if(node->right != NULL) {
            push(stack, node->right);
        }
    }

    for(print_idx; print_idx >= 0; print_idx--) {
        printf("%d ", print_stack[print_idx]);
    }
}