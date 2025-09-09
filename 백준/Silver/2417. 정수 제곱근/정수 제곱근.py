import sys
import bisect

input = sys.stdin.readline
n = int(input().strip())

left, right = 0, n
while left < right:
    mid = ((left + right) // 2)
    
    if (mid * mid) < n:
        left = mid + 1
    else:
        right = mid

print(right)