// 입출력을 사용하기위한 헤더파일
#include <stdio.h>
// malloc같은 동적 메모리 할당할때도 쓰이는 헤더파일
#include <stdlib.h>

#define TRUE 1
#define FALSE 0

#define MAX_VERTICES 100
#define INF 1000

typedef struct GraphType {
    // node
    int node;
    // 인접행렬 : 가중치
    int weight[MAX_VERTICES][MAX_VERTICES];
} GraphType;

// 선택된 노드들을 표현하는 배열
int selected[MAX_VERTICES];
// 거리를 표현하는 배열
int distance[MAX_VERTICES];

void initDistance(GraphType* graph) {
    for(int i=0; i<graph->node; i++) {
        distance[i] = INF;
    }
}

// 최소 거리값을 갖는 정점 반환 함수 : 노드 개수를 인자로 받습니다.
int get_min_vertex(int node_cnt) {
    int return_vertex;
    
    for(int i=0; i<node_cnt; i++) {
        if(!selected[i]) {
            // 선택된 적 없는 노드면, 배열에서 몇 번째 정점인지 인덱스값 할당
            return_vertex = i;
            break;
        }
    }
    // 선택된 적 없는 노드가 거리도 반환정점보다 더 짧으면 해당 인덱스 번호 할당
    for(int i=0; i<node_cnt; i++) {
        if(!selected[i] && (distance[i] < distance[return_vertex])) {
            return_vertex = i;
        }
    }

    return return_vertex;
}

// 인자로 그래프와 시작노드를 입력받음
void prim(GraphType* g, int s) {
    int i, u, v;
    // 정점(노드) 개수만큼 반복
    for(u=0; u < g->node; u++) {
        // 우선 엄청 큰 값으로 초기화
        distance[u] = INF;
    }

    distance[s] = 0;
    // 정점(노드)개수 만큼 반복하며 가장 최소값을 가지는 정점을 찾아 변수에 대입
    for(i=0; i < g->node; i++) {
        u = get_min_vertex(g->node);
            selected[u] = TRUE;

        // 만약 최소값의 정점의 거리가 iNF면 그냥 끝
        if(distance[u] == INF) {
            return;
        }

        // INF 값이 아니라면 출력
        printf("정점 %d 추가\n", u+1);

        for(v=0; v < g->node; v++) {
            // 만약 가중치가 무한이 아니라면
            if(g->weight[u][v] != INF) {
                // 만약 선택되지 않은 정점이고, 가중치갑보다 거리값이 크면
                if(!selected[v] && g->weight[u][v] < distance[v]) {
                    distance[v] = g->weight[u][v];
                }
            }
        }
    }
}

int main(void) {
    // 배열을 이용해서 표현 : (노드가 10개, 인접행렬표현)
    GraphType graph = { 10,
            // 1  2   3    4    5   6   7   8   9  10      
            {{ 0, 3, INF, INF, INF, 11, 12,INF,INF,INF }, //1번 노드의 연결 노드 정보
            { 3,  0, 5, 4, 1, 7, 8,INF,INF,INF }, //2번 노드의 연결 노드 정보
            { INF, 5, 0, 2, INF, INF, 6,5,INF,INF,}, //3번 노드의 연결 노드 정보
            { INF, 4, 2, 0, 13, INF, INF,14,INF,16}, //4번 노드의 연결 노드 정보
            { INF, 1, INF, 13, 0, 9, INF,INF,18,17 }, //5번 노드의 연결 노드 정보
            { 11,7, INF, INF, 9, 0,INF,INF,INF, INF }, //6번 노드의 연결 노드 정보
            { 12,8,6,INF,INF,INF,0,13,INF,INF }, //7번 노드의 연결 노드 정보
            {INF,INF,5,14,INF,INF,13,0,INF,15} , //8번 노드의 연결 노드 정보
            {INF,INF,INF,INF,18,INF,INF,INF,0,10}, //9번 노드의 연결 노드 정보
            {INF,INF,INF,16,17,INF,INF,15,10,0} // 10번 노드의 연결 노드 정보
    }};


}