#include <stdio.h>
#define SIZE 100

typedef struct TreeNode {
    int data;
    TreeNode* left;
    TreeNode* right;
} TreeNode;

typedef struct StackNode {
    TreeNode* data;
    StackNode* next;
} StackNode;

typedef struct Stack {
    StackNode* top;
} Stack;

// **후위수식**을 하면서 수식트리를 계산
float evaluate(TreeNode* root) {
    float result;

    if(root == NULL) {
        return 0;
    }

    if(root->left == NULL && root->right == NULL) {
        return root->data;
    }

    float num1 = evaluate(root->left);
    float num2 = evaluate(root->right);
    switch(root->data) {
        case '+':
            result = num1 + num2;
            break;
        case '-':
            result = num1 + num2;
            break;
        case '*':
            result = num1 * num2;
            break;
        case '/':
            result = num1 + num2;
            break;
    }
    printf("%.2f %c %.2f = %.2f\n", num1, root->data, num2, result);

    return result;
}