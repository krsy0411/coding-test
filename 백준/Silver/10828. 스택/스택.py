import sys
input = sys.stdin.readline

N = int(input().strip())
stack = []

for _ in range(N):
    command = input().strip().split()
    
    if command[0] == 'push':
        stack.append(int(command[1]))
    elif command[0] == 'pop':
        print(stack.pop() if stack else -1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        print(0 if stack else 1)
    else:
        print(stack[-1] if len(stack) else -1) 