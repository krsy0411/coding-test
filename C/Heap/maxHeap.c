#include <stdio.h>
#define MAX_SIZE 100

typedef struct Heap {
    int array[MAX_SIZE]; // 
    int size; // 힙의 사이즈
} Heap;

// 최대힙 초기화
void init(Heap* h) {
    h->size = 0;
}

// 최대힙 내 두 노드 교환
void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// 최대힙에서의 노드 삽입
void insert(Heap* h, int value) {
    if(h->size == MAX_SIZE) {
        printf("힙이 꽉차서 더 넣을 수 없습니다");
        return;
    }
    // 초기값은 가장 끝 노드 인덱스값으로
    int currentIndex = h->size;

    // 삽입할땐 우선 배열의 가장 끝으로 우선 넣어준다
    h->array[currentIndex] = value;
    // 이후, 현인덱스값이 0 이상이고 현위치의 값이 부모노드의 값보다 크면
    while(currentIndex > 0 && h->array[currentIndex] > h->array[(currentIndex-1) / 2]) {
        // 현위치의 값과 부모노드값을 스왑하고
        swap(&h->array[currentIndex], &h->array[(currentIndex - 1) / 2]);
        // 현위치 인덱스값을 부모노드 인덱스값으로 변경
        currentIndex = (currentIndex - 1) / 2;
    }
    
    // 힙의 사이즈 증가
    h->size++;
}

int remove(Heap* h) {
    if(h->size == 0) {
        printf("힙이 비어있어서 더이상 지울 수가 없습니다");
        return -1;
    }
    // 지우려고 하는 시점의 최대값은 항상 루트노드 : 해당 함수의 반환값
    int maxValue = h->array[0];

    // 루트노드에 가장 끝 노드의 값을 할당
    h->array[0] = h->array[h->size - 1];
    // 초기값은 루트노드의 인덱스값으로
    int currentIndex = 0;

    while(1) {
        // 좌측자식노드, 우측자식노드, 가장 큰 값의 인덱스 변수 3개를 생성
        int leftChildIndex = 2*currentIndex + 1;
        int rightChildIndex = 2*currentIndex + 2;
        int largestIndex = currentIndex;

        // 여기서 잠깐 : 왜 우측자식노드에 대한 if문이 더 아래에 위치할까요?
        // 완전이진트리로서, 우측자식노드가 배열의 인덱스값이 더 뒤이기 때문입니다 : 웬만하면 트리의 가장 우측 끝으로 보내는거죠
    
        // 좌측자식노드가 힙 사이즈보다는 작고, 가장 큰 값의 인덱스보다는 값이 크다면
        if(leftChildIndex < h->size && h->array[leftChildIndex] > h->array[largestIndex]) {
            // 가장 큰 값의 인덱스에 좌측자식노드 인덱스 할당
            largestIndex = leftChildIndex;
        }
        // 우측자식노드가 힙 사이즈보다는 작고, 가장 큰 값의 인덱스보다는 값이 크다면
        if(rightChildIndex < h->size && h->array[rightChildIndex] > h->array[largestIndex]) {
            // 가장 큰 값의 인덱스에 우측자식노드 인덱스 할당
            largestIndex = rightChildIndex;
        }
        // 자식노드의 값이 더 큰게 있어서 현 위치 인덱스값과 뭔가 다르면, 스왑을 진행하고, 현 위치 인덱스에 largestIndex값을 할당합니다.
        if(largestIndex != currentIndex) {
            swap(&h->array[currentIndex], &h->array[largestIndex]);
            currentIndex = largestIndex;
        } else {
            // 현위치 인덱스와 largestIndex의 값이 동일하면 그냥 while문을 탈출합니다.
            break;
        }
    }

    return maxValue;
}

void print(Heap* h) {
    print("Max Heap: ");
    for(int i=0; i<h->size; i++) {
        printf("%d ", h->array[i]);
    }
    printf("\n");
}

int main(void) {
    // 포인터 변수로 생성하지 않음
    Heap heap;
    init(&heap);

    insert(&heap, 4);
    insert(&heap, 2);
    insert(&heap, 8);
    insert(&heap, 1);
    insert(&heap, 6);

    printf("제거 전 힙 : ");
    print(&heap);

    int maxValue = remove(&heap);
    if(maxValue != -1) {
        printf("제거된 최대값 : %d\n", maxValue);
    }

    printf("제거 후 힙 : ");
    print(&heap);

    return 0;
}