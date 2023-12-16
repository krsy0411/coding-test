#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define SIZE 20

void RandomNumberInsert(int array[]) {
    srand(time(NULL));

    for(int i=0; i<SIZE; i++) {
        array[i] = rand() * 100; // 0-99까지의 난수를 리스트 안에 넣기
    }
}

void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void selectionSort(int array[]) {
    // 첫번째 인덱스부터 돌면서 비교 후 교환
    for(int i=0; i<SIZE-1; i++) {
        // 우선 최소 인덱스 임의 초기화
        int least = i;

        // i번째 인덱스 이후부터 돌면서
        for(int j=i+1; j<SIZE; j++) {
            // 더 값이 작은게 뒤에서 발견되면
            if(array[j] < array[least]) {
                // 최소 인덱스를 업데이트
                least = j;
            }
        }

        // 스왑
        swap(&array[i], &array[least]);
    }
}

void printArray(int array[]) {
    for(int i=0; i<SIZE; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");
}

int main(void) {
    int array[SIZE];
    RandomNumberInsert(array);

    printf("Original List \n");
    printArray(array);

    selectionSort(array);

    printf("After Selection Sort\n");
    printArray(array);

    return 0;
}