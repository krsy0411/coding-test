import sys
input = sys.stdin.readline

K = int(input().strip())
buildings = list(map(int, input().strip().split()))

def preorder_recursive(buildings, start_i, end_i, level_output, level):
    # 기저 조건
    if start_i > end_i:
        return
    
    middle_i = (start_i + end_i) // 2
    level_output[level].append(buildings[middle_i])
    preorder_recursive(buildings, start_i, middle_i - 1, level_output, level + 1)
    preorder_recursive(buildings, middle_i + 1, end_i, level_output, level + 1)

# 함수 실행
output = [[] for _ in range(K)]
preorder_recursive(buildings, 0, len(buildings) - 1, output, 0)
for i in range(len(output)):
    print(' '.join(map(str,output[i])))