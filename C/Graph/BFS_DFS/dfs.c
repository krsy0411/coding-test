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

// 그래프 초기화
void init(GraphType* graph) {
    int row, column;
    graph->node_cnt = 0;
    for(row=0; row<MAX_VERTICES; row++) {
        for(column=0; column<MAX_VERTICES; column++) {
            graph->adj_matrix[row][column] = 0;
        }
    }
}

// 정점 삽입 함수
void insert_vertex(GraphType* graph, int vertex) {
    if((graph->node_cnt)+1 > MAX_VERTICES) {
        fprintf(stderr, "그래프: 정점의 개수 초과");
		return;
    }
    graph->node_cnt++;
}

// 간선 삽입 함수
void insert_edge(GraphType* graph, int start, int end) {
    if(start >= graph->node_cnt || end >= graph->node_cnt) {
        fprintf(stderr, "그래프: 정점 번호 오류");
		return;
    }
    // 그래프 정점 번호 오류 경우가 아니라면 : 연결되어있음을 표현
    graph->adj_matrix[start][end] = 1;
    graph->adj_matrix[end][start] = 1;
}

void DFS(GraphType* graph, int vertex_index) {
    visited[vertex_index] = TRUE;
    printf("정점 %d", vertex_index);
    
    for(int i=0; i<graph->node_cnt; i++) {
        // 간선이 존재하고 방문한적이 없으면
        if(graph->adj_matrix[vertex_index][i] && !visited[i]) {
            // DFS 실행 : 재귀함수
            DFS(graph, i);
        }
    }
}

int main(void)
{
	GraphType *g = (GraphType *)malloc(sizeof(GraphType));
	init(g);

	for (int i = 0; i<4; i++) {
        insert_vertex(g, i);
    }
	insert_edge(g, 0, 1);
	insert_edge(g, 0, 2);
	insert_edge(g, 0, 3);
	insert_edge(g, 1, 2);
	insert_edge(g, 2, 3);

	printf("깊이 우선 탐색\n");
	DFS(g, 0);
	printf("\n");
	free(g);
	return 0;
}