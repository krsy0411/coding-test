#include <stdio.h>
#include <stdlib.h>

// vertex : 정점 : 최대 개수 설정
#define MAX_VERTICES 50

// 그래프 구조체 정의
typedef struct GraphType {
    int node_cnt;
    // 인접 행렬 방식
    int adj_matrix[MAX_VERTICES][MAX_VERTICES];
} GraphType;

void init(GraphType* graph) {
    int row, column;
    // 우선 정점 개수 0으로 설정 : 초기화니까
    graph->node_cnt = 0;
    // 이중 반복문으로 행렬값 초기화
    for(row=0; row<MAX_VERTICES; row++) {
        for(column=0; column<MAX_VERTICES; column++) {
            graph->adj_matrix[row][column] = 0;
        }
    }
}

void insert_node(GraphType* graph, int node) {
    if((graph->node_cnt+1) > MAX_VERTICES) {
        fprintf(stderr,"overflow!!");
        return;
    }
    graph->node_cnt++;
}

void insert_edge(GraphType* graph, int start, int end) {
    // ????
    if((start >= graph->node_cnt) || (end >= graph->node_cnt)) {
        fprintf(stderr,"vertex key error!!");
        return;
    }
    graph->adj_matrix[start][end] = 1;
    graph->adj_matrix[start][end] = 1;
}

void print_adj_matrix(GraphType* graph) {
    for(int i=0;i<graph->node_cnt;i++){
        for(int j=0;j<graph->node_cnt;j++){
            printf("%2d",graph->adj_matrix[i][j]);
        }
        printf("\n");
    }
}

int main(void) {
    // 포인터 변수 생성
    GraphType* graph;
    // 동적 메모리 할당
    graph = (GraphType*)malloc(sizeof(GraphType));

    init(graph);
    // 정점 4개 생성
    for(int i=0; i<4; i++) {
        insert_node(graph,i);
    }
    // 간선 추가
    insert_edge(graph,0,1);
    insert_edge(graph,0,2);
    insert_edge(graph,0,3);
    insert_edge(graph,1,2);
    insert_edge(graph,1,3);
    insert_edge(graph,2,3);

    // 인접행렬 출력
    print_adj_matrix(graph);

    free(graph);
    return 0;
}