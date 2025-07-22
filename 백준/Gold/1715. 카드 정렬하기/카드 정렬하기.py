import sys
import heapq
input = sys.stdin.readline

N = int(input().strip())
cards = [int(input().strip()) for _ in range(N)]
heapq.heapify(cards)
result = 0 # 결과 : 총 누적합

# 최소힙에서 2개씩 꺼내서 합산 후 다시 힙에 추가 -> 반복
while len(cards) >= 2:
	num_first = heapq.heappop(cards)
	num_second = heapq.heappop(cards)
	sum_result = (num_first + num_second)
	
	# 힙에 합산 결과를 넣고 결과를 누적
	heapq.heappush(cards, sum_result)
	result += sum_result 
	
print(result)