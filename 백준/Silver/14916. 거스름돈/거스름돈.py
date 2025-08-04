import sys
input = sys.stdin.readline

n = int(input().strip())
result = 0

result = n // 5
n = n % 5
while n % 2 != 0:
    result -= 1
    if result < 0:
        print(-1)
        exit()
    n += 5

if n % 2 == 0:
    result += (n // 2)
    print(result)
else:
    print(-1)