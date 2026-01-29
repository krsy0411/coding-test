import sys
import heapq

# 입력
input = sys.stdin.readline
heap = []
result = []

N = int(input().strip())
# 로직 수행
for _ in range(N):
    x = int(input().strip())
    
    if x != 0:
        heapq.heappush(heap, (abs(x),x)) # 튜플 : (절댓값, 원본)
    else:
        if heap:
            result.append(heapq.heappop(heap)[1])
        else:
            result.append(0)
            
# 출력
print('\n'.join(map(str, result)))