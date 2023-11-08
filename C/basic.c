#include <stdio.h>
#include <stdlib.h>

// 구조체
struct Point {
    int x;
    int y;
};
// 인스턴스 생성
struct Point MyPoint = {30, 40};
// 포인터 변수 생성
struct Point* ptr = &MyPoint;

// 타입 별칭
typedef struct tagPoint {
    int x;
    int y;
} Point1;

Point1 MyPoint1 = {30, 40};
Point1* ptr = &MyPoint1;