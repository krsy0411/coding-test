import sys
input = sys.stdin.readline

N = int(input().strip())

meetings = []
for _ in range(N):
    start, end = map(int, input().strip().split())
    meetings.append((start, end))
meetings.sort(key=lambda x: (x[1], x[0]))  # 종료 시간 기준으로 정렬

count = 0
last_end_time = 0
for start, end in meetings:
    if start >= last_end_time:
        count += 1
        last_end_time = end
        
# 결과 출력
print(count)