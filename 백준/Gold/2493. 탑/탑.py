import sys
input = sys.stdin.readline

N = int(input().strip())
inputs = list(map(int, input().strip().split()))
stack = []

for i in range(N):
    current_input = inputs[i]
    
    while stack and stack[-1][0] < current_input:
        stack.pop()
    
    if stack:
        print(stack[-1][1], end=' ')
    else:
        print(0, end=' ')

    stack.append((current_input, i+1))