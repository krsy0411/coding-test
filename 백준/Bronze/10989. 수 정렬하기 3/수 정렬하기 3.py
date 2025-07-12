import sys
input = sys.stdin.readline

N = int(input().strip())
arr = [0 for _ in range(10000)]
for _ in range(N):
    num = int(input().strip())
    arr[num-1] += 1

for i in range(10000):
    for j in range(arr[i]):
        sys.stdout.write(str(i+1) + '\n')
