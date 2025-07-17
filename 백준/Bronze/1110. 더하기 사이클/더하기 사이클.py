# 백준 1110번 문제: 더하기 사이클
import sys
input = sys.stdin.readline

N = int(input().strip())
result = 0 # 사이클 수
temp_n = N

while True:    
    ten_digit = temp_n // 10 
    one_digit = temp_n % 10
    
    if temp_n < 10:
        temp_n = one_digit * 10 + one_digit
    else:
        temp_n = one_digit * 10 + (ten_digit + one_digit) % 10
    
    result += 1
    
    if temp_n == N:
        break

print(result)