# 백준 11279 : 최대 힙
import sys
import heapq
input = sys.stdin.readline

N = int(input().strip())
pq = []
result = [] # 결과출력용 값 모음 배열

for _ in range(N):
    x = int(input().strip()) # 연산에 대한 정보를 나타내는 정수x
    
    if x == 0:
        num = -heapq.heappop(pq) if pq else 0 # 값이 있다면 힙에서 값 꺼낼때 반대 부호 적용(최대힙처럼 동작하도록 했기 때문에)
        result.append(num)
    else:
        heapq.heappush(pq, -x) # 최대 힙처럼 동작하도록 음수로
    
sys.stdout.write('\n'.join(map(str, result)) + '\n')