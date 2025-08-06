import sys
input = sys.stdin.readline

input_string = input().strip()
arr = input_string.split('.') # . 기준 분할 -> 빈 문자열 또는 값

for i in range(len(arr)):
    # 빈 문자열이면 패스
    if arr[i] == '':
        continue
    
    length_x = len(arr[i])
    # X가 홀수개면 -1 출력하고 반복문 탈출
    if length_x % 2 == 1:
        print(-1)
        exit()
    
    transformed_str = '' # arr에 치환해서 넣을 변환된 문자열
    transformed_str += ('AAAA' * (length_x // 4))
    length_x %= 4
    transformed_str += ('BB' * (length_x // 2))
    
    arr[i] = transformed_str
    
print('.'.join(arr))