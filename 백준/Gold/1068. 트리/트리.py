import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 입력값 처리
N = int(input().strip())
parent_node_nums = list(map(int, input().strip().split()))
deleted_node = int(input().strip())

root_node = 0
graph = [[] for _ in range(N)]
for current_node, parent_node in enumerate(parent_node_nums):
    # 루트 노드 설정
    if parent_node == -1:
        root_node = current_node
    else:
        # 관계 설정
        graph[parent_node].append(current_node)
        
# 재귀함수 정의
def recursive_count(node):
    # 삭제 노드인 경우
    if node == deleted_node:
        return 0
    
    # 리프 노드인 경우
    if not graph[node]:
        return 1
    
    cnt = 0
    for next_node in graph[node]:
        cnt += recursive_count(next_node)
        
    return cnt

# 삭제 노드를 부모의 자식 목록에서도 제거
if deleted_node != root_node:
    parent = parent_node_nums[deleted_node]
    graph[parent].remove(deleted_node)

# 함수 실행 & 결과 출력
total_leaf_nodes_cnt = recursive_count(root_node)
print(total_leaf_nodes_cnt if root_node != deleted_node else 0)