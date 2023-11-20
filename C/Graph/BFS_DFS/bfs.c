#include <stdio.h>
#include <stdlib.h>

#define TRUE 1
#define FALSE 0
#define MAX_QUEUE_SIZE 10
#define MAX_VERTICES 50

typedef struct {
    int queue[MAX_QUEUE_SIZE];
    // 큐의 전방 포인터 인덱스값
    int front;
    // 큐의 후방 포인터 인덱스값
    int rear;
} QueueType;

int visited[MAX_VERTICES];
typedef struct {
    // 그래프 노드 개수
    int node_cnt;
    // 인접행렬형태
    int adj_matrix[MAX_VERTICES][MAX_VERTICES];
} GraphType;

// 큐 초기화 함수
void queue_init(QueueType* q) {
    // 다 0으로 초기화
    q->front = q->rear = 0;
}

// 공백상태검출 함수
int is_empty(QueueType* q) {
    return (q->front == q->rear);
}
// 큐 포화상태검출 함수
int is_full(QueueType* q) {
    return ((q->rear+1) % MAX_QUEUE_SIZE == q->front);
}

// 큐 삽입 함수
void insert_queue(QueueType* q, int item) {
    if(is_full(q)) {
        fprintf(stderr, "큐가 포화상태입니다.");
        return;
    }
    q->rear = (q->rear + 1) % MAX_QUEUE_SIZE;
    // 맨 후방에 넣고자하는 값 넣기
    q->queue[q->rear] = item;
}

// 큐 삭제 함수
int delete_queue(QueueType* q) {
    if(is_empty(q)) {
        fprintf(stderr, "큐가 공백상태입니다.");
        return;
    }
    q->front = (q->front+1) % MAX_QUEUE_SIZE;
    // 큐는 선입선출 구조
    return q->queue[q->front];
}

void graph_init(GraphType* g) {
    // 노드 개수 0으로 초기화
    g->node_cnt = 0;
    for(int row=0; row<MAX_VERTICES; row++) {
        for(int column=0; column<MAX_VERTICES; column++) {
            // 인접행렬의 내부 값들도 다 0으로 초기화
            g->adj_matrix[row][column] = 0;
        }
    }
}

void insert_vertex(GraphType* g, int vertex) {
    if((g->node_cnt) + 1 > MAX_VERTICES) {
        fprintf(stderr, "그래프: 정점의 개수 초과");
		return;
    } 
    // 정점 추가 - 노드 개수 증가
    g->node_cnt++;
}

void insert_edge(GraphType* g, int start, int end) {
    if(start >= g->node_cnt || end >= g->node_cnt) {
        fprintf(stderr, "그래프: 정점 번호 오류");
		return;
    }
    // 가중치를 지닌 간선은 아님(무방향)
    g->adj_matrix[start][end] = 1;
    g->adj_matrix[end][start] = 1;
}

void BFS(GraphType* g, int vertex_index) {
    QueueType* q;
    // 큐 초기화
    queue_init(&q);
    visited[vertex_index] = TRUE;
    printf("%d  방문 -> ", vertex_index);
    // 시작 정점을 큐에 저장
    insert_queue(&q, vertex_index);

    while(!is_empty(&q)) {
        // 큐에서 값 하나 추출
       int vertex = delete_queue(&q);
        // 큐에서 추출한 값과 인접한 노드들을 순회하며
        for(int w=0; w<g->node_cnt; w++) {
            // 방문한적이 없으면
            if(g->adj_matrix[vertex][w] && !visited[w]) {
                // 방문처리하고
                visited[w] = TRUE;
                printf("%d 방문 -> ", w);
                // 해당 노드를 큐에 집어넣는다
				insert_queue(&q, w);
            }
        }
    }
}

int main(void) {
    GraphType* graph = (GraphType *)malloc(sizeof(GraphType));
    // 그래프 초기화
    graph_init(graph);
    // 그래프에 정점 넣기
    for(int i=0; i<6; i++) {
        insert_vertex(graph, i);
    }
    // 그래프에 간선 넣기
	insert_edge(graph, 0, 2);
	insert_edge(graph, 2, 1);
	insert_edge(graph, 2, 3);
	insert_edge(graph, 0, 4);
	insert_edge(graph, 4, 5);
	insert_edge(graph, 1, 5);

	printf("너비 우선 탐색\n");
	BFS(graph, 0);
	printf("\n");
	free(graph);

	return 0;
}