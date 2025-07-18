import sys
input = sys.stdin.readline

N, B = map(int, input().strip().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().strip().split())))

# 행렬 곱셈 함수
def matrix_multiply(matrix_a, matrix_b):
    result = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
            result[i][j] %= 1000 # 나머지 연산
    
    return result

# 행렬 곱셈을 거듭제곱법을 사용해서 줄여내기
def half_exponential(matrix, exp):
    if exp == 1:
        return [[element % 1000 for element in row] for row in matrix]
    
    half = half_exponential(matrix, exp // 2)
    half_multiply_result = matrix_multiply(half, half)
    if exp % 2 == 0:
        return half_multiply_result
    else:
        return matrix_multiply(half_multiply_result, matrix)
    
result = half_exponential(graph, B)
for row in result:
    print(' '.join(map(str, row)))