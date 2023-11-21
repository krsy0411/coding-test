#include <stdio.h>
// 퀵정렬 지원하는 호출문(qsort) : void qsort (void *base, size_t nel, size_t width, int (*compare)(const void *, const void *);
// base: 정렬하고자 하는 배열의 포인터, nel: 배열의 각 원소들의 총 수, width: 배열에서 원소 하나의 크기, (*compare): 비교를 수행할 함수 포인터
#include <stdlib.h>

#define TRUE 1
#define FALSE 0

#define MAX_VERTICES 100
#define INF 1000

int parent[MAX_VERTICES];

typedef struct Edge {
    int start, end, weight;
} Edge;

typedef struct GraphType {
    int n; // 노드 개수
    Edge edges[2* MAX_VERTICES];
} GraphType;

void set_init(int n) {
    for(int i=0; i<n; i++) {
        parent[i] = -1;
    }
}

// 현재 노드가 속하는 집합 반환
int set_find(int currentNode) {
    // 방문하지않은 노드라면 그대로 반환
    if(parent[currentNode] == -1) {
        return currentNode;
    }
    // 방문한 노드인 경우 : 
    while(parent[currentNode] != -1) {
        currentNode = parent[currentNode];
    }

    return currentNode;
}

void set_union(int a, int b) {
    int root1 = set_find(a);
    int root2 = set_find(b);

    // 노드 두개의 루트가 다르면 집합을 합해준다
    if(root1 != root2) {
        parent[root1] = root2;
    }
}

void graph_init(GraphType* g) {
    // 노드 개수 0개로
    g->n = 0;

    for(int i=0; i<2*MAX_VERTICES; i++) {
        g->edges[i].start = 0;
        g->edges[i].end = 0;
        g->edges[i].weight = INF;
    } 
}

void insert_edge(GraphType* g, int start, int end, int weight) {
    g->edges[g->n].start = start;
    g->edges[g->n].end = end;
    g->edges[g->n].weight = weight;
    g->n++;
}

int compare(Edge* a, Edge* b) {
    Edge* x = a;
    Edge* y = b;

    return (x->weight - y->weight);
}

void Kruskal(GraphType* g) {
    int edge_accepted = 0;
    int u_set, v_set; // 정점들의 집합 번호

    Edge e;
    qsort(g->edges, g->n, sizeof(Edge *), compare);
    
    printf("크루스칼 최소 신장 트리 알고리즘 \n");
    
    int i=0;
    while(edge_accepted < (g->n - 1)) {
        e = g->edges[i];
        u_set = set_find(e.start);
        v_set = set_find(e.end);

        // 집합이 서로 다르면
        if(u_set != v_set) {

            printf("간선 (%d,%d) %d 선택\n", e.start, e.end, e.weight);
            edge_accepted++;
            set_union(u_set, v_set);
        }
        i++;
    }
}

int main(void) {
    GraphType* g;
    g = (GraphType *)malloc(sizeof(GraphType));

    graph_init(g);

    insert_edge(g, 0, 1, 29);
    insert_edge(g, 1, 2, 16);
    insert_edge(g, 2, 3, 12);
    insert_edge(g, 3, 4, 22);
    insert_edge(g, 4, 5, 27);
    insert_edge(g, 5, 0, 10);
    insert_edge(g, 6, 1, 15);
    insert_edge(g, 6, 3, 18);
    insert_edge(g, 6, 4, 25);

    Kruskal(g);
    
    free(g);
    return 0;
}