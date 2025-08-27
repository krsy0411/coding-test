import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())

def recursive_find_sequence(depth, temp_result, visited):
    # 기저조건
    if depth == M:
        print(' '.join(map(str, temp_result)))
        return

    for next_node in range(1, N + 1):
        if (not visited[next_node]) and (temp_result[-1] < next_node):
            visited[next_node] = True
            temp_result.append(next_node)
            recursive_find_sequence(depth + 1, temp_result, visited)
            visited[next_node] = False
            temp_result.pop()

# 실행
for node in range(1, N + 1):
    visited = [False] * (N + 1)
    visited[node] = True
    recursive_find_sequence(1, [node], visited)