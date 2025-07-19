# 백준 1655 : 카드 정렬하기
import heapq
import sys
input = sys.stdin.readline

N = int(input().strip())
pq = [int(input().strip()) for _ in range(N)] 
heapq.heapify(pq) # 힙 만들기 : 최소힙

result = 0 # 최소한의 비교횟수
while len(pq) > 1:
    num_first = heapq.heappop(pq)
    num_second = heapq.heappop(pq)
    temp_sum = num_first + num_second
    result += temp_sum
    
    heapq.heappush(pq, temp_sum)
    
print(result)