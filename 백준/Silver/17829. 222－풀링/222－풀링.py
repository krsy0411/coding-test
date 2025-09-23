import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N = int(input().strip()) # N: 행렬 크기
matrix = [list(map(int, input().strip().split())) for _ in range(N)] # N x N 행렬 입력처리

def recursive_two_by_two_pooling(matrix):
    current_size = len(matrix)
    
    if current_size == 1:
        return matrix[0][0]
    
    new_size = current_size // 2
    new_matrix = [[0] * new_size for _ in range(new_size)]
    
    for i in range(new_size):
        for j in range(new_size):
            two_by_two_block = [matrix[2*i][2*j], matrix[2*i][2*j+1], matrix[2*i+1][2*j], matrix[2*i+1][2*j+1]]
            two_by_two_block.sort()
            new_matrix[i][j] = two_by_two_block[2] # 각 2x2 블록에서 두 번째로 큰 값 선택

    return recursive_two_by_two_pooling(new_matrix)

result = recursive_two_by_two_pooling(matrix)
print(result)