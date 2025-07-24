# 백준 9935 : 프린터 큐
import sys
from collections import deque
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n, m = map(int, input().strip().split())
    queue = list(map(int, input().strip().split()))

    # 중요도와 함께 인덱스를 저장
    printer_queue = deque([(i, queue[i]) for i in range(n)])
    count = 0 # 출력된 문서의 개수
    
    # 현재 큐의 가장 앞 요소의 중요도를 확인
    # 가장 앞 요소의 중요도가 가장 큰지 확인
    while printer_queue:
        current = printer_queue[0]
        is_highest = True
        for i in range(1, len(printer_queue)):
            if current[1] < printer_queue[i][1]:
                # 현재 요소보다 더 중요한 요소가 있다면
                printer_queue.append(printer_queue.popleft())
                is_highest = False
                break
        # 현재 요소가 가장 중요하다면
        if is_highest:
            count += 1
            idx, val = printer_queue.popleft()
            if idx == m:
                print(count)
                break