#include <stdio.h>

typedef struct TreeNode {
    int data;
    struct TreeNode* left;
    struct TreeNode* right;
} TreeNode;

// 링크표현법과 배열표현법 두 가지를 이용해 순회
// Link : 왼쪽, 오른쪽 포인터 이용 : 자식 노드 방문
// Array : index*2 == 왼쪽, index*2+1 == 오른쪽 : 자식 노드 방문

// 전위 순회 : V-L-R
void linkPreorder(TreeNode* node) {
    if(node) {
        // root
        printf("%d ", node->data);
        // left
        linkPreorder(node->left);
        // right
        linkPreorder(node->right);
    }
}
void arrPreorder(int arr[], int idx) {
    if(arr[idx] != 0) {
        int left = idx*2;
        int right = idx*2+1;

        printf("%d ", arr[idx]);
        arrPreorder(arr, left);
        arrPreorder(arr, right);
    }
}

// 중위 순회 : L-V-R
void linkInorder(TreeNode* node) {
    if(node) {
        // left
        linkInorder(node->left);
        // root
        printf("%d ", node->data);
        // right
        linkInorder(node->right);
    }
}
void arrInorder(int arr[], int idx) {
    if(arr[idx] != 0) {
    int left = idx*2;
    int right = idx*2+1;

    arrInorder(arr, left);
    printf("%d ", arr[idx]);
    arrInorder(arr, right);
    }
}

// 후위 순회 : L-R-V
void linkPostOrder(TreeNode* node) {
    if(node) {
        linkPostOrder(node->left);
        linkPostOrder(node->right);
        printf("%d ", node->data);
    }
}
void arrPostOrder(int arr[], int idx) {
    if(arr[idx] != 0) {
        int left = idx*2;
        int right = idx*2+1;

        arrPostOrder(arr, left);
        arrPostOrder(arr, right);
        printf("$d ", arr[idx]);
    }
}


int main() {
    // Link
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
    TreeNode* root = &n1;

    // 전위 순회
    linkPreorder(root);
    // 중위 순회
    linkInorder(root);
    // 후위 순회
    linkPostOrder(root);

    // 배열표현법을 이용한 트리 생성 : 0번째 인덱스는 -1로 값을 주고, 나머지 중에 NULL인 값들도 -1로 처리 : -1은 NULL을 의미
    int node[16] = {-1, 1, 2, 7, 3, 6, 8, 9, 4, 5, -1, -1, -1, -1, 10, 11};

    // 전위 순회
    arrPreorder(node, 1);
    // 중위 순회
    arrInorder(node, 1);
    // 후위 순회
    arrPostOrder(node, 1);

    return 0;
}