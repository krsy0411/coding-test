#include <stdio.h>

typedef struct TreeNode {
    int data;
    struct TreeNode* left;
    struct TreeNode* right;
} TreeNode;

// 링크표현법의 트리 생성 방식은 두가지가 존재 : malloc or {}

// malloc 이용 방식
TreeNode* createNode(int data) {
    struct TreeNode* newNode = (TreeNode*)malloc(sizeof(TreeNode*));
    newNode->data = data;
    // 다른 노드와 연결까지는 하지 않음
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

int main() {
    // malloc 이용방식일때, 화살표를 이용해서 링크 연결
    TreeNode* root = createNode(1);
    root->left = createNode(2);
    root->left->left = createNode(3);
    root->left->left->left = createNode(4);
    root->left->left->right = createNode(5);
    root->left->right = createNode(6);
    root->right = createNode(7);
    root->right->left = createNode(8);
    root->right->right = createNode(9);
    root->right->right->left = createNode(10);
    root->right->right->left = createNode(11);

    // {} 방법일때,
    TreeNode n1 = {4,NULL, NULL};
    TreeNode n2 = {5,NULL, NULL};
    TreeNode n3 = {10,NULL, NULL};
    TreeNode n4 = {11,NULL, NULL};
    TreeNode n5 = {3,&n1, &n2};
    TreeNode n6 = {6,NULL, NULL};
    TreeNode n7 = {8,NULL, NULL};
    TreeNode n8 = {9,&n3, &n4};
    TreeNode n9 = {2,&n5, &n3};
    TreeNode n10 = {7,&n7, &n8};
    TreeNode n111 = {1,&n9, &n10};
    TreeNode* root_bracket_link = &n1;

    ////////////////////////////////////////
    // 배열표현법을 이용한 트리 생성 : 0번째 인덱스는 -1로 값을 주고, 나머지 중에 NULL인 값들도 -1로 처리 : -1은 NULL을 의미
    int node[16] = {-1, 1, 2, 7, 3, 6, 8, 9, 4, 5, -1, -1, -1, -1, 10, 11};

    return 0;
}