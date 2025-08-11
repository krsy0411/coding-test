# 백준 1935 : 후위 표기식2
import sys

input = sys.stdin.readline

N = int(input().strip())
strings = list(input().strip())

# 입력값 처리
dictionary = dict((string, 0) for string in strings if string.isalpha())
keys = []
for s in strings:
    if s.isalpha() and s not in keys:
        keys.append(s)

for i in range(N):
    num = int(input().strip())
    dictionary[keys[i]] = num # 순차적으로 값 갱신

# 후위 표기식 계산
stack = []
for string in strings:
    if string.isalpha():
        stack.append(dictionary[string]) # 알파벳에 해당하는 숫자값 보관
    else:
        num1 = stack.pop()
        num2 = stack.pop()
        temp = 0
        
        if string == '+':
            temp = (num2 + num1)
        elif string == '-':
            temp = (num2 - num1)
        elif string == '*':
            temp = (num2 * num1)
        elif string == '/':
            temp = (num2 / num1)

        stack.append(temp)
            
print(f"{stack[0]:.2f}")