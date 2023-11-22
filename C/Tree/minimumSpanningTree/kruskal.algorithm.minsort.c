#include <stdio.h>
#include <stdlib.h>

// 간선 구조체
typedef struct {
    int start, end, weight;
} Edge;

// 그래프 구조체
typedef struct {
    int vertex, edge;
    Edge* edges;
} Graph;

// 최소힙 구조체
typedef struct {
    Edge* arr;
    int size;
    int capacity;
} MinHeap;

// 최소힙 생성
MinHeap* createMinHeap(int capacity) {
    MinHeap* heap = (MinHeap *)malloc(sizeof(MinHeap));

    heap->arr = (Edge *)malloc(sizeof(Edge) * capacity);
    heap->size = 0;
    heap->capacity = capacity;

    return heap;
}

// 최소힙을 유지시키기 위해 배열을 위로 재배치시키는 함수
void HeapifyUp(MinHeap* heap, int index) {
    int parent = (index-1) / 2;
    while(index>0 && heap->arr[index].weight < heap->arr[parent].weight) {
        // 부모와 위치 교환
        Edge temp = heap->arr[index]; // 값 잠시 보유(포인터X)
        // 값 교환
        heap->arr[index] = heap->arr[parent];
        heap->arr[parent] = temp;
        // 인덱스도 교환
        index = parent;
        parent = (index-1)/2;
    }
}

// 최소힙 속성을 유지하도록 배열을 아래로 재배치
void heapifyDown(MinHeap* heap, int index) {
    int leftChild = 2*index + 1;
    int rightChild = 2*index + 2;

    int smallest = index;

    if(leftChild < heap->size && heap->arr[leftChild].weight < heap->arr[smallest].weight) {
        smallest = leftChild;
    }

    if(rightChild < heap->size && heap->arr[rightChild].weight < heap->arr[smallest].weight) {
        smallest = rightChild;
    }

    if(smallest != index) {
        Edge temp = heap->arr[index];
        heap->arr[index] = heap->arr[smallest];
        heap->arr[smallest] = temp;

        heapifyDown(heap, smallest);
    }
}

// 간선 삽입
void insertEdge(MinHeap* heap, Edge key) {
    // 현재 힙의 사이즈가 용량과 같으면 간선을 넣을 수가 없다
    if(heap->size == heap->capacity) {
        printf("Heap is full. Cannot insert edge.\n");
        return;
    }
    // 힙의 끝에 값을 추가
    heap->arr[heap->size] = key;
    // 힙과 삽입하고자하는 값의 인덱스 전달
    HeapifyUp(heap, heap->size);
}

Edge extractMinimum(MinHeap* heap) {
    // 최소힙의 루트값이 가장 작은 값
    Edge minEdge = heap->arr[0];

    // 힙의 가장 아래 값을 루트로 이동시키고 내려가면서 재배치
    heap->arr[0] = heap->arr[heap->size -1];
    heap->size--;
    heapifyDown(heap, 0);

    return minEdge;
}

void Kruskal(Graph* graph) {
    int vertex = graph->vertex;
    // 최소신장트리의 간선 수는 정점-1
    Edge* result = (Edge*)malloc((vertex-1) * sizeof(Edge));

    // 그래프의 간선을 최소힙에 삽입
    MinHeap* heap = createMinHeap(graph->edge);
    for (int i = 0; i < graph->edge; ++i) {
        insert(heap, graph->edges[i]);
    }

    int *parent = (int *)malloc(vertex * sizeof(int));
    for (int v = 0; v < vertex; ++v) {
        parent[v] = v; // 각 노드를 자신의 부모로 초기화
    }

    int edgeCount = 0; // 최소신장트리의 현재 간선 수

    // 크루스칼 알고리즘 수행
    while (edgeCount < vertex - 1) {
        Edge nextEdge = extractMinimum(heap);

        // 사이클이 형성되지 않으면 간선을 최소신장트리에 추가
        int x = nextEdge.start;
        int y = nextEdge.end;
        int xRoot = x;
        int yRoot = y;

        // 각 노드의 루트를 찾음
        while (parent[xRoot] != xRoot) {
            xRoot = parent[xRoot];
        }

        while (parent[yRoot] != yRoot) {
            yRoot = parent[yRoot];
        }

        // 루트가 다르다면 사이클이 형성되지 않음
        if (xRoot != yRoot) {
            result[edgeCount++] = nextEdge;
            // 두 트리를 합침 (한 트리의 루트를 다른 트리의 루트의 부모로 설정)
            parent[yRoot] = xRoot;
        }
    }

    // 최소신장트리 출력
    printf("Edges in Minimum Spanning Tree:\n");
    for (int i = 0; i < vertex - 1; ++i) {
        printf("(%d - %d) with weight %d\n", result[i].start, result[i].end, result[i].weight);
    }

    // 메모리 해제
    free(result);
    free(heap->arr);
    free(heap);
    free(parent);
}