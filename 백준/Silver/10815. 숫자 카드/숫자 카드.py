# 백준 10815 : 숫자 카드
import sys
input = sys.stdin.readline

n = int(input().strip())
cards = set(map(int, input().strip().split()))

m = int(input().strip())
result = []
nums = list(map(int, input().strip().split()))
for num in nums:
    if num in cards:
        result.append(1)
    else:
        result.append(0)
        
print(' '.join(map(str, result)))