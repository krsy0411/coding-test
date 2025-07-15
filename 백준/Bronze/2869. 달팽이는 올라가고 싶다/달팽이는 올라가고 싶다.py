import sys
import math

input = sys.stdin.readline
A,B,V = list(map(int, input().strip().split()))

day = A - B # 올라가는 높이 - 내려가는 높이
result = math.ceil((V-A) / day) + 1
sys.stdout.write(f"{result}\n")