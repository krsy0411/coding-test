import sys

input = sys.stdin.readline
h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))

t1 = h1 * 3600 + m1 * 60 + s1 # 현재 시간
t2 = h2 * 3600 + m2 * 60 + s2 # 던지는 시간
result_time = 0

if t1 < t2:
    result_time = t2 - t1
elif t1 > t2:
    result_time = 24 * 3600 - (t1 - t2)
else:
    result_time = 24 * 3600

h = result_time // 3600
m = (result_time % 3600) // 60
s = (result_time % 3600) % 60

print(f"{h:02}:{m:02}:{s:02}")