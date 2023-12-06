#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 1000

typedef struct heap {
    int data[MAX_SIZE];
    int size;
} heap;

void init(heap* heap) {
    heap->size = 0;
}

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void insert(heap* heap, int data) {
    if(heap->size == MAX_SIZE) {
        printf("힙이 꽉 차서 더 넣을 수가 없습니다 \n");
        return;
    }

    // 삽입할 데이터가 위치할 위치의 인덱스값을 표현한 변수 : 항상 초기값은 맨 끝 인덱스로(즉, 서브트리 제일 끝으로)
    int insertedPositionIdx = heap->size;

    // 위치의 인덱스값이 1(루트)가 아니고 넣을 데이터가 현 위치의 루트노드의 값보다 작은 경우 : 최소힙이니까 최대한 올라가야함
    while((insertedPositionIdx != 1) && (data < heap->data[insertedPositionIdx / 2])) {
        // 부모노드와 현위치(넣을 데이터)노드의 값 변경
        swap(&heap->data[insertedPositionIdx/2], &heap->data[insertedPositionIdx]);
    }

    // 노드 삽입했으니까 힙의 사이즈 증가
    heap->size++;
}

// 힙의 사이즈가 0이라 삭제할 노드가 없으면 0, 아닌 경우엔 해당 위치 값
int delete(heap* heap) {
    if(heap->size == 0) {
        return -1;
    }

    // 삭제할때는 루트 노드를 지우고 재조합함
    int minData = heap->data[0];
    // 가장 끝 노드(서브트리의 가장 끝으로 들어온 값)를 루트노드로
    heap->data[0] = heap->data[heap->size - 1];
    heap->size--;

    // 루트노드를 삭제하고 힙을 유지시키기 위해 돌리는 과정

    // 루트노드부터 자식노드들과 비교하면서 내려가기
    int currentIndex = 0;
    while(1) {
        int leftChildIndex = 2 * currentIndex + 1;
        int rightChildIndex = 2 * currentIndex + 2;
        int smallestIndex = currentIndex;

        // 항상 우선 왼쪽자식노드부터 확인

        // 왼쪽 자식 노드 인덱스가 사이즈보다 작고, 현재 가장 작은 값의 인덱스(부모 노드의 인덱스)의 데이터가 왼쪽 자식노드 인덱스의 데이터값보다 크면
        if (leftChildIndex < heap->size && heap->data[leftChildIndex] < heap->data[smallestIndex]) {
            // 부모노드 인덱스를 왼쪽 자식 노드로 할당
            smallestIndex = leftChildIndex;
        }
        // 오른쪽자식노드인덱스가 사이즈보다 작고, 부모노드의 데이터값이 오른쪽자식노드의 데이터값보다 크면
        if (rightChildIndex < heap->size && heap->data[rightChildIndex] < heap->data[smallestIndex]) {
            // 부모노드 인덱스를 오른쪽 자식 노드로 할당
            smallestIndex = rightChildIndex;
        }
        // 만약 가장작은값의 인덱스가 자식노드 인덱스로 내려가면서 현위치 인덱스값과 다르면
        if (smallestIndex != currentIndex) {
            // 부모-노드 값 스왑
            swap(&heap->data[currentIndex], &heap->data[smallestIndex]);
            // 현위치인덱스값을 갱신
            currentIndex = smallestIndex;
        } else {
            // 나머지 경우 : 가장작은값의 인덱스와 현위치 인덱스값이 동일한 경우 : 즉, 자식노드로 내려가지 않는 경우 : 탈출
            break;
        }
    }
    // 삭제되는 최소값(루트노드)은 반환
    return minData;
}

void print(heap* heap) {
    print("Heap: ");
    for (int i = 0; i < heap->size; i++) {
        printf("%d ", heap->data[i]);
    }
    printf("\n");
}