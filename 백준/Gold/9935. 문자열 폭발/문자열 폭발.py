# 백준 9935 : 문자열 폭발
import sys
input = sys.stdin.readline

strings = input().strip()
string_bomb = input().strip()

stack = []
bomb_length = len(string_bomb)

for char in strings:
    stack.append(char)
    
    # 마지막 문자열이 폭발 문자열과 같은지 확인
    if len(stack) >= bomb_length and ''.join(stack[-bomb_length:]) == string_bomb:
        for _ in range(bomb_length):
            stack.pop()
    
# 남은 문자열을 출력
result = ''.join(stack)
print(result if result else "FRULA")