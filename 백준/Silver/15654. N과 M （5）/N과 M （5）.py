import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
nums = list(map(int, input().strip().split()))
nums.sort()

def recursive_find_sequence(depth, visited, temp_result):
    # 기저 조건 : 출력 & 반환
    if depth == M:
        print(' '.join(map(str, temp_result)))
        return
    
    for next_node in nums:
        if next_node not in visited:
            visited.add(next_node)
            temp_result.append(next_node)
            recursive_find_sequence(depth + 1, visited, temp_result)
            visited.remove(next_node)
            temp_result.pop()
    # 아무것도 반환하지 않음
    return


# 실행
for start_node in nums:
    visited = set()
    visited.add(start_node)
    
    recursive_find_sequence(1, visited, [start_node])