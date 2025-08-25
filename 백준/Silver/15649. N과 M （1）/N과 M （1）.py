import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())

def recursive_find_sequence(depth, visited, temp_result):
    # 기저 조건 : 깊이가 M과 동일해지면 종료
    if depth == M:
        print(' '.join(map(str, temp_result)))
        return  

    for next_node in range(1, N + 1):
        if not visited[next_node]:
            visited[next_node] = True
            temp_result.append(next_node)
            recursive_find_sequence(depth + 1, visited, temp_result)
            temp_result.pop()
            visited[next_node] = False

    # 아무 반환값 없이 종료
    return



# 함수 실행 & 결과 출력
for i in range(1, N + 1):
    visited = [False] * (N + 1)
    visited[i] = True
    recursive_find_sequence(1, visited, [i])