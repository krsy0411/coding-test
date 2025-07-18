import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().strip().split()))

def binary_search(list, target):
    start = 0
    end = len(list)

    while start < end:
        mid = (start + end) // 2

        if list[mid] < target:
            start = mid + 1
        else:
            end = mid

    return start # 삽입할 인덱스

def solve(A):
    list = []
    
    for value in A:
        index = binary_search(list, value)
        if index == len(list):
            list.append(value)
        else:
            list[index] = value

    return len(list)

print(solve(A))