import sys
import bisect

input = sys.stdin.readline
n, m = map(int, input().split())

dots = list(map(int, input().strip().split()))
dots.sort()

for _ in range(m):
    start, end = map(int, input().split())
    left_idx = bisect.bisect_left(dots, start)
    right_idx = bisect.bisect_right(dots, end)
    
    print(right_idx - left_idx)