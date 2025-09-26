import sys

input = sys.stdin.readline
K = int(input().strip()) # K번째 수

# K번째 수가 0인지 1인지 판단하는 함수
def is_one(k):
    if k == 1:
        return 0
    if k == 2:
        return 1
    if k % 2 == 0:
        # 짝수면 절반 위치의 수를 뒤집음
        return 1 - is_one(k // 2)
    else:
        # 홀수면 (k+1)/2 위치의 수와 동일
        return is_one((k + 1) // 2)
    
print(is_one(K))