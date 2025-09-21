import sys
input = sys.stdin.readline

n = int(input().strip())
x = list(map(int, input().strip().split()))

answer = 0
sum_x = sum(x)

for xi in x:
    sum_x -= xi
    answer += (xi * sum_x)
    
print(answer)