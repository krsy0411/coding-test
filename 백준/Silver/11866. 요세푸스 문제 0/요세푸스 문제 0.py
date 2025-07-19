# 백준 11866 : 요세푸스 문제 0
from collections import deque
import sys
input = sys.stdin.readline

N,K = map(int, input().strip().split())
queue = deque([i+1 for i in range(N)])
result = []

while queue:
    # k-1개만큼 빼서 뒤로 다시 추가
    for _ in range(K-1):
        back_num = queue.popleft()
        queue.append(back_num)
    # k번째 숫자는 큐에서 빼고 출력
    remove_num = queue.popleft()
    result.append(remove_num)

print("<" + ", ".join(map(str, result)) + ">")