# 백준 2504 : 괄호의 값
import sys
input = sys.stdin.readline

brackets = list(input().strip()) # 괄호열
stack = [] # 열린괄호들을 쌓아두는 스택
result = 0
temp_result = 1

for i in range(len(brackets)):
    bracket = brackets[i]
    
    if bracket == '(':
        stack.append(bracket)
        temp_result *= 2
    elif bracket == '[':
        stack.append(bracket)
        temp_result *= 3
    elif bracket == ')':
        # 스택이 비어있거나 괄호쌍이 안 맞는 경우
        if (not stack) or (stack[-1] != '('):
            result = 0
            break
        
        # 바로 이전 문자가 열린 괄호라면
        if brackets[i-1] == '(':
            result += temp_result

        temp_result //= 2
        stack.pop()
    elif bracket == ']':
        # 스택이 비어있거나 괄호쌍이 안 맞는 경우
        if (not stack) or (stack[-1] != '['):
            result = 0
            break
        
        # 바로 이전 문자가 열린 괄호라면
        if brackets[i-1] == '[':
            result += temp_result
            
        temp_result //= 3
        stack.pop()
        
# 아직 스택에 열린 괄호가 남았다면
if stack:
    result = 0
print(result)