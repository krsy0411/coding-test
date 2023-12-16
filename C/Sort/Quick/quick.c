#include <stdio.h>
#include <stdlib.h> //srand, rand를 사용하기 위한 헤더파일
#include <time.h> // time을 사용하기 위한 헤더파일

void swap(int* value1, int* value2) {
    int temp = *value1;

    *value1 = *value2;
    *value2 = temp;
}

void printArray(int* data, int size) {
    for(int i=0; i<size; i++) {
        printf("%d ", data[i]);
    }
    printf("\n");
}

void arrayInitRandomly(int* data, int size) {
    for(int i=0; i<size; i++) {
        data[i] = rand() % 100; // 0-99 사이의 수 뽑아서 배열에 넣기
    }
}

void quickSort(int* data, int start_index, int end_index) {
    // 시작지점과 끝지점의 인덱스가 동일하거나 시작지점 인덱스가 더 크면 바로 정렬 끝내기
    if(start_index >= end_index) {
        return;
    }
    int pivot_index = start_index;
    int low_idx = start_index+1;
    int high_idx = end_index;

    // low index가 high index보다 작거나 같을 동안에만 수행
    while(low_idx <= high_idx) {
        // 피벗인덱스의 데이터보다 값이 작은 동안엔
        while(data[low_idx] <= data[pivot_index]) {
            // 계속 인덱스를 높임
            low_idx++;
        }
        // 피벗인덱스의 데이터보다 값이 큰 동안 & 인덱스값이 시작지점보단 큰 동안
        while(data[high_idx] >= data[pivot_index] && high_idx > start_index) {
            // 인덱스를 계속 내림
            high_idx--;
        }
        // 만약 인덱스가 서로 엇갈렸다면
        if(low_idx > high_idx) {
            // high index의 데이터와 pivot index의 데이터를 서로 바꿔줍니다
            swap(&data[high_idx], &data[pivot_index]);
        } else {
            // low index, high index가 서로 엇갈리지 않았다면 : low,high 인덱스의 값을 위치 교환
            swap(&data[high_idx], &data[low_idx]);
        }

        // 정렬 이후 왼쪽
        quickSort(data, start_index, high_idx-1);
        // 정렬 이후 오른쪽
        quickSort(data, high_idx+1, end_index);
    }
}

int main(void) {
    // 입력받을 데이터 : 배열 사이즈
    int arr_size;

    // 입력받는 코드 줄
    printf("배열 사이즈 입력: ");
    // 사용자가 입력한 배열 사이즈를 변수 안에 넣기
    scanf("%d", &arr_size);
    // 입력받은 배열 사이즈를 토대로 데이터 크기맞춰서 배열 생성
    int data[arr_size];

    // 사용자로부터 입력받은 데이터 기반으로 배열 초기화
    arrayInitRandomly(data, arr_size);

    // 퀵 정렬 수행
    quickSort(data, 0, arr_size-1);
    // 출력
    printArray(data, arr_size);
    return 0;
}