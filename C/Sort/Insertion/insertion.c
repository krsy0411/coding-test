#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define SIZE 20

int count = 0;

void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// 랜덤으로 난수 20개를 만드는 함수
void RandomArray(int array[]) {
    srand(time(NULL));
    for(int i=0; i<SIZE; i++) {
        array[i] = rand() % 100; // 0부터 99까지의 난수를 생성한 후 리스트에 저장
    }
}

// 프린트 함수
void printArray(int array[]) {
    for(int i=0; i<SIZE; i++) {
        printf("%d\t", array[i]);
    }
    printf("\n");
}

void insertionSort(int array[]) {
    // 1번째 인덱스부터 반복 시작
    for(int i=1; i<SIZE; i++) {
        int key = array[i];
        // 비교할 값들의 인덱스는 현 위치의 왼쪽들을 비교 : 따라서 i-1값으로 설정
        int j = i-1;

        // j인덱스값이 0이상이고, 키값보다는 크다면
        while(j >= 0 && array[j] > key) {
            // 해당 값을 하나씩 윗 인덱스로 옮기고, j값은 -1해주기 : 실제 값을 옮기는 행동X, 인덱스값만 변경
            array[j+1] = array[j];
            j = j-1;
        }

        // 키값 위치 업데이트 : 실제 값 업데이트
        array[j+1] = key;
    }
}

int main(void) {
    int array[20];
    RandomArray(array);

    insertionSort(array);

    printf("삽입 정렬 : \n");
    printArray(array);
    
    return 0;
}