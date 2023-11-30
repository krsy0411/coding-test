#include <stdio.h>
#include <stdlib.h>

#define TRUE 1
#define FALSE 0
#define MAX_VERTICES 100	
#define INF	1000000

typedef struct GraphType {
    int node_cnt;
    int weight[MAX_VERTICES][MAX_VERTICES];
} GraphType;

/* 시작정점으로부터의 최단경로 거리 */
int distance[MAX_VERTICES];
// 방문 여부 처리
int found[MAX_VERTICES];

// 최단거리 노드 번호 고르는 함수
int choose_smallest_index(int distance[], int n, int found[]) {
    // from <limits.h>
    int min = INF;
    int minPosition = -1;

    for(int i=0; i<n; i++) {
        if(distance[i] < min && !found[i]) {
            min = distance[i];
            minPosition = i;
        }
    }

    return minPosition;
}

void print_status(GraphType* graph) {
    printf("distance: ");

    for(int i=0; i<graph->node_cnt; i++) {
        if(distance[i] == INF) {
            printf(" * ");
        } else {
            printf("%2d ", distance[i]);
        }
    }
    printf("\n\n");
}

void shortest_path(GraphType* graph, int startNodeNumber) {
    int array[10] = {1,};
    // 초기화
    for(int i=0; i<graph->node_cnt; i++) {
        // 해당 노드와 연결된 노드는 해당노드까지의 거리 + 간선거리니까 우선 해당노드까지의 거리로 입력
        distance[i] = graph->weight[startNodeNumber][i];
        found[i] = FALSE;
    }
    // 시작 정점 방문 표시
    found[startNodeNumber] = TRUE;
    distance[startNodeNumber] = 0;
    for(int i=0; i<graph->node_cnt-1; i++) {
        print_status(graph);

        int u = choose(distance, graph->node_cnt, found);
        array[i+1] = u+1;
    }
}