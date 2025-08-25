import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())

def recursive_find_sequence(depth, temp_result):
    # 기저조건 : 깊이가 M가 동일해지면 출력
    if depth == M:
        print(' '.join(map(str, temp_result)))
        return
    
    for next_node in range(1, N+1):
        temp_result.append(next_node)
        recursive_find_sequence(depth + 1, temp_result)
        temp_result.pop()
    
    return

# 실행
for start_node in range(1, N + 1):
    recursive_find_sequence(1, [start_node])