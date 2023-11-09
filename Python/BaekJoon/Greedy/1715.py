import sys
import heapq

result = 0
n = int(input())

data_list = []
for _ in range(n):
  data_list.append(int(sys.stdin.readline().rstrip()))
data_list.sort()

heapq.heapify(data_list)
while len(data_list) != 1:
  # 파이썬에서 힙 라이브러리는 최소힙이므로 항상 최상단 노드가 최솟값이다
  first = heapq.heappop(data_list)
  second = heapq.heappop(data_list)
  heapq.heappush(data_list, first+second)
  result += (first+second)

print(result)