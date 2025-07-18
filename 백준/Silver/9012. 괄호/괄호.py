import sys
input = sys.stdin.readline
T = int(input().strip()) # 테스트 케이스 개수

for _ in range(T):
    parenthesis = list(input().strip())
    stack = []
    result = 'YES'
    
    # 우선 홀수개면 무조건 답 아님
    if len(parenthesis) % 2 != 0:
        print('NO')
        continue
    
    for par in parenthesis:
        if par == '(':
            stack.append('(')
        else:
            if not stack:
                result = 'NO'
                break
            stack.pop()

    if stack:
        result = 'NO'
    
    print(result)