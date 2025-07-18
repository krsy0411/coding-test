import sys
input = sys.stdin.readline
N = int(input().strip())

stack = []
for _ in range(N):
    num = int(input().strip())
    stack.append(num)

result = 0 # 결과값
max_h = 0 # 현재까지의 최고 높이
while stack:
    num = stack.pop()
    
    if max_h < num:
        max_h = num
        result += 1
        
print(result)