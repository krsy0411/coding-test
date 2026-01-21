import sys
input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())
MAX_NUM = 1000
MIN_NUM = -999

for x in range(MIN_NUM, MAX_NUM):
    for y in range(MIN_NUM, MAX_NUM):
        if a*x + b*y == c and d*x + e*y == f:
            print(x, y)
            sys.exit()