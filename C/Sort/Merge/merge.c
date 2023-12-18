#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define SIZE 20

void randomlyInsertNumber(int array[]) {
    srand(time(NULL));

    for(int i=0; i<SIZE; i++) {
        array[i] = rand() & 100;
    }
}

void printValueOfArray(int array[]) {
    for(int i=0; i<SIZE; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");
}

// 뱡힙정렬을 수행하는 역할의 함수
void mergeSort(int array[], int left, int right) {
    if(left < right) {
        int middle = (left + right) / 2;

        // 재귀함수 : 2개의 부분 리스트로 다시 정렬 수행
        mergeSort(array, left, middle); // 부분 리스트 중 앞쪽 리스트 
        mergeSort(array, middle+1, right); // 부분 리스트 중 뒤쪽 리스트

        // 재귀호출이 끝난 이후, 두 부분 리스트를 병합(merge)
        
    }   
}

// 부분 리스트를 다시 병합시켜주는 역할의 함수
void merge(int array[], int left, int middle, int right) {
    int start = left;
    int result = left;

    int leftArrayCnt = middle - left + 1;
    int rightArrayCnt = right - middle;
    // 임시 배열 생성
    int leftArray[leftArrayCnt], rightArray[rightArrayCnt];
    
    // 데이터 복사해서 임시 생성한 배열에 값 넣어주기
    for(int i=0; i<leftArrayCnt; i++) {
        leftArray[i] = array[left+i];
    }
    for(int j=0; j<rightArrayCnt; j++) {
        rightArray[j] = array[middle+1+j];
    }

    // 두개의 부분리스트를 합치기
    int i=0, j=0, k=left;
    while(i < leftArrayCnt && j < rightArrayCnt) {
        if(leftArray[i] <= rightArray[j]) {
            array[k] = leftArray[i];
            i++;
        } else {
            array[k] = rightArray[j];
            j++;
        }
        k++;
    }

    // 부분리스트에서 남은 요소들 복사
    while(i < leftArrayCnt) {
        array[k] = leftArray[i];
        i++;
        k++;
    }
    while(j < rightArrayCnt) {
        array[k] = rightArray[j];
        j++;
        k++;
    }
}


int main(void) {
    int array[SIZE];
    randomlyInsertNumber(array);

    printf("정렬 전 배열 : \n");
    printValueOfArray(array);

    mergeSort(array, 0, SIZE-1);

    printf("정렬 후 배열 : \n");
    printValueOfArray(array);
}