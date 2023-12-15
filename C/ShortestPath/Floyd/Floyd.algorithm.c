#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define MAX_VERTICES 100 // 최대 정점 개수
#define INF 100000 // 무한대(연결이 없는 경우)

typedef struct Graph {
    int node_cnt;
    int weight[MAX_VERTICES][MAX_VERTICES];
} Graph;

// 최단경로를 표현하는 2차원 배열
int parent[MAX_VERTICES][MAX_VERTICES];

void Floyd(Graph* graph) {
    for(int i=0; i<graph->node_cnt; i++) {
        for(int j=0; j<graph->node_cnt; j++) {
            parent[i][j] = graph->weight[i][j];
        }
    }
    for(int k=0; k<graph->node_cnt; k++) {
        for(int i=0; i<graph->node_cnt; i++) {
            for(int j=0; j<graph->node_cnt; j++) {
                if(parent[i][k] + parent[k][j] < parent[i][j]) {
                    parent[i][j] = parent[i][k] + parent[k][j];
                }
            }
        }
    }
}

int main(void) {
    Graph graph = {10,
    // 1  2   3    4    5   6    7  8  9   10  
	{{ 0, 3, INF, INF, INF, 11, 12,INF,INF,INF },//1
	{ 3,  0, 5, 4, 1, 7, 8,INF,INF,INF },// 2
	{ INF, 5, 0, 2, INF, INF, 6,5,INF,INF,},// 3
	{ INF, 4, 2, 0, 13, INF, INF,14,INF,16},// 4
	{ INF, 1, INF, 13, 0, 9, INF,INF,18,17 },// 5
	{ 11,7, INF, INF, 9, 0,INF,INF,INF, INF },// 6
	{ 12,8,6,INF,INF,INF,0,13,INF,INF }, // 7
    {INF,INF,5,14,INF,INF,13,0,INF,15} , // 8
    {INF,INF,INF,INF,18,INF,INF,INF,0,10}, // 9
    {INF,INF,INF,16,17,INF,INF,15,10,0} // 10
    }};

    Floyd(&graph);

    printf("Floyd-Warshall Algorithm\n");
    for(int i=0; i<graph.node_cnt; i++) {
        for(int j=0; j<graph.node_cnt; j++) {
            if(parent[i][j] == INF) {
                printf("INF\t");
            } else {
                printf("%d\t", parent[i][j]);
            }
        }
    }

    return 0;
}