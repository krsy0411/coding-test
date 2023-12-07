#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define TRUE 1
#define FALSE 0
#define MAX_VERTICES 100 // 최대 정점 개수
#define INF	1000000 // 무한대를 의미하는 수

typedef struct Graph {
    // 노드 개수
    int node_cnt;
    // 가중치
    int weight[MAX_VERTICES][MAX_VERTICES]; // 인접행렬 방식
} Graph;

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

void print_status(Graph* graph) {
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

// 초기화 함수
void init(Graph* graph, int startNumber) {
    for(int i=0; i<graph->node_cnt; i++) {
        // 해당 노드와 연결된 노드는 해당노드까지의 거리 + 간선거리니까 우선 해당노드까지의 거리로 입력
        distance[i] = graph->weight[startNumber][i];
        // 방문처리 배열의 모든값을 false로 초기화
        found[i] = FALSE;
    }
}

void shortest_path(Graph* graph, int startNodeNumber) {
    int array[10] = {1,};
    // 초기화
    init(graph, startNodeNumber);

    // 시작 정점 방문 표시
    found[startNodeNumber] = TRUE;
    // 시작 정점의 거리는 0
    distance[startNodeNumber] = 0;
    for(int i=0; i<graph->node_cnt-1; i++) {
        print_status(graph);

        int smallestIndex = choose_smallest_index(distance, graph->node_cnt, found);
        array[i+1] = smallestIndex+1;
        found[smallestIndex] = TRUE;

        for(int j=0; j<graph->node_cnt; j++) {
            // 만약 방문하지 않았다면 진입
            if(!found[j]) {
                // 지금까지의 가장 작은 거리 + 이동할 거리의 합이 현재 거리값보다 작으면 진입
                if((distance[smallestIndex] + graph->weight[smallestIndex][j]) < distance[j]) {
                    // 현재 거리값을 합으로 업데이트
                    distance[j] = distance[smallestIndex] + graph->weight[smallestIndex][j];
                }
            }
        }
    }
}

int main(void) {
    // 인접행렬 방식
    Graph g = { 10,
        // 각 노드들 순서대로 가중치 표현
        {{ 0, 3, INF, INF, INF, 11, 12,INF,INF,INF },
        { 3,  0, 5, 4, 1, 7, 8,INF,INF,INF },
        { INF, 5, 0, 2, INF, INF, 6,5,INF,INF,},
        { INF, 4, 2, 0, 13, INF, INF,14,INF,16},
        { INF, 1, INF, 13, 0, 9, INF,INF,18,17 },
        { 11,7, INF, INF, 9, 0,INF,INF,INF, INF },
        { 12,8,6,INF,INF,INF,0,13,INF,INF }, 
        {INF,INF,5,14,INF,INF,13,0,INF,15} , 
        {INF,INF,INF,INF,18,INF,INF,INF,0,10}, 
        {INF,INF,INF,16,17,INF,INF,15,10,0}}
	};

    printf("인접 행렬을 이용하여 구현하기\n");
    shortest_path(&g, 0);
    return 0;
}