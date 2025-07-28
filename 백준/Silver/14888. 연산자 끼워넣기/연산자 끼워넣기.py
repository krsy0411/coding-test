# 백준 2294 : 연산자 끼워넣기
import sys
N = int(input().strip())
A = list(map(int, input().strip().split())) # 수열 A
operators = list(map(int, input().strip().split())) # 연산자 개수 : 덧셈, 뺄셈, 곱셈, 나눗셈

max_num = -float('inf')
min_num = float('inf')
def dfs(depth, current_num, plus, minus, multiply, division):
    global max_num
    global min_num
    
    if depth == N:
        max_num = max(max_num, current_num)
        min_num = min(min_num, current_num)
        return
    
    if plus > 0:
        dfs(depth + 1, current_num + A[depth], plus - 1, minus, multiply, division)
    if minus > 0:
        dfs(depth+1, current_num - A[depth], plus, minus-1, multiply, division)
    if multiply > 0:
        dfs(depth+1, current_num * A[depth], plus, minus, multiply-1, division)
    if division > 0:
        if current_num < 0:
            dfs(depth+1, -(-current_num // A[depth]), plus, minus, multiply, division-1)
        else:
            dfs(depth+1, current_num // A[depth], plus, minus, multiply, division-1)
            
dfs(1, A[0], operators[0], operators[1], operators[2], operators[3])
sys.stdout.write(f"{max_num}\n{min_num}")