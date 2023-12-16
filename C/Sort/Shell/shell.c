#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define SIZE 20

void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void printArray(int array[]) {
    for(int i=0; i<SIZE; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");
}

void randomNumberInsertTo(int array[]) {
    srand(time(NULL));

    for(int i=0; i<SIZE; i++) {
        array[i] = rand() % 100;
    }
}

// 현재 잘 이해가 안 가는 코드
void shellSort(int array[]) {
    // 간격 설정해서 순회
    for(int gap = SIZE/2; gap>0; gap /= 2) {
        // 간격 내에서 배열 끝까지 순회하며 정렬 수행
        for(int i=gap; i<SIZE; i++) {
            int temp = array[i];
            int j;

            for(j=i; j>=gap && array[j-gap] > temp; j -= gap) {
                array[j] = array[j-gap];
            }
            array[j] = temp;
        }
    }
}


int main(void) {
    int array[SIZE];
    randomNumberInsertTo(array);

    printf("정렬 전 배열: \n");
    printArray(array);

    shellSort(array);
    printf("정렬 후 배열: \n");
    printArray(array);

    return 0;
}