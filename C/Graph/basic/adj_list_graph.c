#include <stdio.h>
#include <stdlib.h>

#define MAX_VERTICES 50

// 인접 리스트 방식의 그래프는 하나의 구조체가 더 필요합니다.
typedef struct GraphNode {
    int value;
    struct GraphNode* link;
} GraphNode;

typedef struct GraphType {
    int node_cnt;
    GraphNode* adj_list[MAX_VERTICES];
} GraphType;

void init(GraphType* graph) {
    graph->node_cnt = 0;

    for(int i=0; i < MAX_VERTICES; i++) {
        graph->adj_list[i] = NULL;
    }
}

void insert_node(GraphType* graph, int node) {
    if((graph->node_cnt)+1 > MAX_VERTICES) {
        fprintf(stderr, "overflow");
        return;
    }
    graph->node_cnt++;
}

void insert_edge(GraphType* graph, int start, int vertex_value) {
    GraphNode* node = (GraphNode*)malloc(sizeof(GraphNode));

    if(start >= graph->node_cnt || vertex_value >= graph->node_cnt) {
        fprintf(stderr,"vertex key error!!");
        return;
    }

    node->value = vertex_value;
    // 출발지점과 도착지점의 링크 생성
    node->link = graph->adj_list[start];
    // ????
    graph->adj_list[start] = node;
}

void print_adj_list(GraphType* graph) {
    for(int i=0; i<graph->node_cnt; i++) {
        GraphNode* node = graph->adj_list[i];
        printf("정점 %d의 인접 리스트",i);
        // 노드가 안 비어있을때까지 반복
        while(node != NULL) {
            printf("-> %d", node->value);
            node = node->link;
        }
        printf("\n");
    }
}

int main(void) {
    GraphType* g;

    g=(GraphType*)malloc(sizeof(GraphType));
    init(g);

    for(int i=0;i<4;i++)
        insert_vertex(g,i);
        
    insert_edge(g,0,1);
    insert_edge(g,1,0);
    insert_edge(g,0,2);
    insert_edge(g,2,0);
    insert_edge(g,0,3);
    insert_edge(g,3,0);
    insert_edge(g,1,2);
    insert_edge(g,2,1);
    insert_edge(g,2,3);
    insert_edge(g,3,2);
    print_adj_list(g);

    free(g);

    return 0;
}