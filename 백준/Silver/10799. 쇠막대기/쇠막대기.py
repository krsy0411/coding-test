import sys

input = sys.stdin.readline
brackets = input().strip()
stack = []
result = 0
prev = ''

for bracket in brackets:
    if bracket == '(':
        stack.append(bracket)
    else:
        stack.pop()
        
        if prev == '(':
            result += len(stack) # 레이저인 경우
        else:
            result += 1 # 막대기 끝인 경우
    
    prev = bracket
    
print(result)