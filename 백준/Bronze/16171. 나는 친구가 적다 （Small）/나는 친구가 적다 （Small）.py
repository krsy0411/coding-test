import sys
input = sys.stdin.readline

S = input()
K = input()
# 문자열만 필터링해서 다시 문자열로 붙이기
filtered_s = ''.join(char for char in S if not char.isdigit())

# 결과 출력
if K in filtered_s:
    print(1)
else:
    print(0)