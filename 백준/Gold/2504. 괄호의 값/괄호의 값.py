import sys
input = sys.stdin.readline

galhos = list(input().strip())
result = 0 # 결과값
temp_result = 1 # 괄호값을 임시 반영하기 위한 변수

stack = []
for i in range(len(galhos)):
	galho = galhos[i]
	
	if galho == '(':
		stack.append(galho)
		temp_result *= 2
	elif galho == '[':
		stack.append(galho)
		temp_result *= 3
	elif galho == ')':
		if (not stack) or (stack[-1] != '('):
			result = 0
			break
		
		if galhos[i-1] == '(':
			result += temp_result
			
		stack.pop()
		temp_result //= 2
	elif galho == ']':
		if (not stack) or (stack[-1] != '['):
			result = 0
			break
	
		if galhos[i-1] == '[':
			result += temp_result
			
		stack.pop()
		temp_result //= 3

# 마지막 검증 : 아직 스택이 안 비었다면 0 출력
if stack:
	print(0)
else:
	print(result)