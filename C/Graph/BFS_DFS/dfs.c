#include <stdio.h>
#include <stdlib.h>

#define TRUE 1
#define FALSE 0
#define MAX_VERTICES 50

// 방문여부 관리 배열
int visited[MAX_VERTICES];
// 그래프 타입 구조체 설정
typedef struct GraphType {
    int node_cnt;
    int adj_matrix[MAX_VERTICES][MAX_VERTICES];
} GraphType;

void init(GraphType* graph) {
    
}