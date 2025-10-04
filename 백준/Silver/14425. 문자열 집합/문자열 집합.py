# 백준 14425 : 문자열 집합
import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())
data = set()

for _ in range(N):
    word = input().strip()
    data.add(word)

result = 0
for _ in range(M):
    word = input().strip()
    
    if word in data:
        result += 1
        
print(result)