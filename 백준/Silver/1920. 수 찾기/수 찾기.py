import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
A.sort()

M = int(input().strip())
B = list(map(int, input().split()))

# 이진 탐색 구현
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

for target_number in B:
    print(binary_search(A, target_number))