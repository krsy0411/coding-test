import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())
coins = [int(input().strip()) for _ in range(n)]

count = 0
for coin in reversed(coins):
    if k == 0:
        break
    
    count += k // coin
    k %= coin
    
print(count)