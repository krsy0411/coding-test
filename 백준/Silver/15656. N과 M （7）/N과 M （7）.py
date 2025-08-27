import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
nums = list(map(int, input().strip().split()))
nums.sort()

def recursive_find_sequence(depth, temp_result):
    if depth == M:
        print(' '.join(map(str, temp_result)))
        return
    
    for next_node in nums:
        temp_result.append(next_node)
        recursive_find_sequence(depth + 1, temp_result)
        temp_result.pop()

    return
    
# 실행
for node in nums:
    recursive_find_sequence(1, [node])