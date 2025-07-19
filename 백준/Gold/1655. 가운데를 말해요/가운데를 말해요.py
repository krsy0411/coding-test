# 백준 1655 : 가운데를 말해요
import heapq
import sys
input = sys.stdin.readline

N = int(input().strip())
max_heap = [] # 중간값 이하
min_heap = [] # 중간값 초과

for _ in range(N):
    n = int(input().strip())
    
    # max_heap이 비어있거나 중간값보다 작거나 같은 경우
    if (not max_heap) or (-max_heap[0] >= n):
        # 최대힙에 원소를 추가하고 중간값 출력
        heapq.heappush(max_heap, -n)
    else:
        # min_heap에 추가하는 경우 : 최소힙에 원소를 추가하고 중간값 출력
        heapq.heappush(min_heap, n)
        
    # 최대/최소힙 간 균형 맞추기
    if len(max_heap) < len(min_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
    elif len(max_heap) > len(min_heap) + 1:
        # 최대힙이 최소힙보다 2개 이상 많은거면 중간값을 유지하지 못하는 경우 -> 최대힙에서 최소힙으로 원소 넘기기
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
    
    # 결과 출력
    print(-max_heap[0])