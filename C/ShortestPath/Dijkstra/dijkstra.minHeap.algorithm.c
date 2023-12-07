#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define TRUE 1
#define FALSE 0
#define MAX_VERTICES 100 // 정점 최대개수
#define INF 1000000 // 무한대 값 정의

// 시작노드로부터의 거리 정의
int distance[MAX_VERTICES];
// 방문여부 처리 배열 정의
int found[MAX_VERTICES];

// 그래프 내 하나의 노드의 구조체 정의
typedef struct GraphNode {
    int node; // 해당 노드의 값
    int weight; // 가중치
    GraphNode* link; // 다음 노드를 가리키는 변수
} GraphNode;

// 그래프의 형태(구조체) 정의
typedef struct Graph {
    int nodes_cnt; // 그래프 내 노드들의 개수
    GraphNode* adj_matrix[MAX_VERTICES]; // 그래프를 표현하는 인접리스트(원소 : 노드 구조체)
} Graph;

// 출력함수
void print(Graph* graph) {
    // 거리 출력
    printf("Distance: ");
    // 노드 개수만큼 순회
    for(int i=0; i<graph->nodes_cnt; i++) {
        if(distance[i] == INF) {
            printf(" * ");
        } else {
            printf("%2d ", distance[i]);
        }
    }
    printf("\n");
    // 방문노드들 출력
    printf("found: ");
    for(int i=0; i<graph->nodes_cnt; i++) {
        if(found[i] == FALSE) {
            printf(" * ");
        } else {
            printf("%2d ", found[i]);
        }
    }
    printf("\n");
}

// 초기화 함수
void init(Graph* graph, int startNumber) {
    for(int i=0; i<graph->nodes_cnt; i++) {
        distance[i] = INF;
        found[i] = FALSE;
    }
    // 시작노드의 거리는 0
    distance[startNumber] = 0;
}

void addEdge(Graph* graph, int start, int end, int weight) {
    GraphNode* newNode = (GraphNode *)malloc(sizeof(GraphNode));
    newNode->node = end;
    newNode->weight = weight;
    // 노드들끼리 연결
    newNode->link = graph->adj_matrix[start];
    graph->adj_matrix[start] = newNode;
}

// 최단거리 노드 번호 반환 함수
int chooseSmallestIndex(int distance[], int found[], int node) {
    int min = INF;
    int minPosition = -1;

    for(int i=0; i<node; i++) {
        if(distance[i] < min && !found[i]) {
            min = distance[i];
            minPosition = i;
        }
    }

    return minPosition;
}

// 다익스트라의 핵심 : 최단경로 찾기함수
void shortest_path(Graph* g, int start)
{
	int i, u, w;
	GraphNode* p;
    int arr[10] ={1,};
	for (i = 0; i < g->nodes_cnt; i++) /* 초기화 */
	{
		distance[i] = INF;
		found[i] = FALSE;
	}
	distance[start] = 0;
	for (i = 0; i < g->nodes_cnt - 1; i++) {
		u = choose(distance, g->nodes_cnt, found);
		found[u] = TRUE;
        arr[i+1] = u+1;
		for (p = g->adj_matrix[u]; p != NULL; p = p->link) {
			w = p->node;
			if (!found[w])
				if (distance[u] + p->weight < distance[w])
					distance[w] = distance[u] + p->weight;
		}
        print_status(g);
	}
        for(int i = 0 ; i <10;i++){
        printf(" %d ", arr[i]);
    }
}

int main(void) {
    Graph graph;
    graph.nodes_cnt = 10;

    for(int i=0; i<graph.nodes_cnt; i++) {
        graph.adj_matrix[i] = NULL;
    }

    printf("2. 연결리스트를 이용하여 구현하기\n");
	add_edge(&graph, 0, 1, 3);
	add_edge(&graph, 0, 5, 11);
	add_edge(&graph, 0, 6, 12);

	add_edge(&graph, 1, 0, 3);
	add_edge(&graph, 1, 2, 5);
	add_edge(&graph, 1, 3, 4);
	add_edge(&graph, 1, 4, 1);
	add_edge(&graph, 1, 5, 7);
	add_edge(&graph, 1, 6, 8);

	add_edge(&graph, 2, 1, 5);
	add_edge(&graph, 2, 3, 2);
	add_edge(&graph, 2, 6, 6);
	add_edge(&graph, 2, 7, 5);

	add_edge(&graph, 3, 1, 4);
	add_edge(&graph, 3, 2, 2);
	add_edge(&graph, 3, 4, 13);
	add_edge(&graph, 3, 7, 14);
	add_edge(&graph, 3, 9, 16);

	add_edge(&graph, 4, 1, 1);
	add_edge(&graph, 4, 3, 13);
	add_edge(&graph, 4, 5, 9);
	add_edge(&graph, 4, 8, 18);
	add_edge(&graph, 4, 9, 17);

	add_edge(&graph, 5, 0, 11);
	add_edge(&graph, 5, 1, 7);
	add_edge(&graph, 5, 4, 9);

	add_edge(&graph, 6, 0, 12);
	add_edge(&graph, 6, 1, 8);
	add_edge(&graph, 6, 2, 6);
	add_edge(&graph, 6, 7, 13);

	add_edge(&graph, 7, 2, 5);
	add_edge(&graph, 7, 3, 14);
	add_edge(&graph, 7, 6, 13);
	add_edge(&graph, 7, 8, 15);

	add_edge(&graph, 8, 4, 18);
	add_edge(&graph, 8, 7, 13);
	add_edge(&graph, 8, 9, 15);

	add_edge(&graph, 9, 4, 16);
	add_edge(&graph, 9, 8, 10);

	shortest_path(&graph, 0);

    return 0;
}