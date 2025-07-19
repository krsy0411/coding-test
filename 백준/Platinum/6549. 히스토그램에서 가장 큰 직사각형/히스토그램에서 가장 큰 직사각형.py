# 백준 6549 : 히스토그램에서 가장 큰 직사각형
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

inputs = []
while True:
    line = input().strip()
    
    if line == '0':
        break
    
    line = list(map(int, line.split()))
    arr = line[1:]
    inputs.append(arr)

def get_middle_area(arr, start, mid, end):
    min_height = arr[mid]
    max_area = min_height
    low, high = mid, mid

    while start < low or end > high:
        # 오른쪽으로 확장하는 경우
        if high < end and (low == start or arr[low - 1] < arr[high + 1]):
            high += 1
            min_height = min(min_height, arr[high])
        else:
            # 왼쪽으로 확장하는 경우
            low -= 1
            min_height = min(min_height, arr[low])

        # 현재 넓이 계산
        width = high - low + 1
        max_area = max(max_area, min_height * width)
    
    return max_area
    
def get_max_area(arr, start, end):
    if start > end:
        return 0
    
    # 막대가 하나인 경우
    if start == end:
        return arr[start]
    
    mid = (start + end) // 2
    left_area = get_max_area(arr, start, mid - 1)
    right_area = get_max_area(arr, mid + 1, end)
    middle_area = get_middle_area(arr, start, mid, end)
    
    return max(left_area, right_area, middle_area)

for arr in inputs:
    print(get_max_area(arr, 0, len(arr) - 1))