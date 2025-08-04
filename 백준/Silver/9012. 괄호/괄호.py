import sys
input = sys.stdin.readline

N = int(input().strip())

for _ in range(N):
    is_all_pair = True
    
    stack = []
    ps = list(input().strip())
    for ps_string in ps:
        if ps_string == '(':
            stack.append(ps_string)
        else:
            if stack:
                stack.pop()
            else:
                is_all_pair = False
                break

    # 여전히 스택에 남아있다면
    if stack:
        is_all_pair = False

    # 결과 출력
    print('YES' if is_all_pair == True else 'NO')