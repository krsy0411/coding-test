import sys
import heapq

input = sys.stdin.readline

N = int(input().strip())

min_heap = []
for _ in range(N):
    nums = map(int, input().split())
    for num in nums:
        heapq.heappush(min_heap, num)
        
        # N개를 계속 유지
        if len(min_heap) > N:
            heapq.heappop(min_heap)
        
print(min_heap[0]) # N번째로 큰 수를 출력