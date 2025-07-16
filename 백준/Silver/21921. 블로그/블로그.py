import sys
input = sys.stdin.readline

N, X = map(int, input().split())
visitors = list(map(int, input().split()))

curr_sum = sum(visitors[:X])
max_sum = curr_sum
count = 1

for i in range(X, N):
    curr_sum += visitors[i] - visitors[i - X]
    
    if curr_sum > max_sum:
        max_sum = curr_sum 
        count = 1 # 새로운 최대값이 발견되면 카운트 초기화
    elif curr_sum == max_sum:
        count += 1

if max_sum == 0:
    print("SAD")
else:
    print(f"{max_sum}\n{count}")