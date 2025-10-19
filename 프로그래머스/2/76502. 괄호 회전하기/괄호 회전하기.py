from collections import deque

def check(current_list, stack):
    result = True
    
    bracket_map = {')': '(', ']': '[', '}': '{'}
    for char in current_list:
        if char in '({[':
                stack.append(char)
        elif char in ')}]':
            if (not stack) or (stack.pop() != bracket_map[char]):
                result = False
                break
    
    return result

def solution(s):
    answer = 0 # 올바른 괄호 문자열이 안 만들어지면 0 유지
    rotate_num = len(s) # 회전 횟수
    queue = deque(list(s))
    
    bracket_map = {
        ')': '(', 
        ']': '[', 
        '}': '{'
    }
    for _ in range(rotate_num):
        # 큐 회전
        queue.append(queue.popleft())
        
        # 스택 이용해서 올바른 짝을 이루는지 체크
        stack = []
        current_list = list(queue)
        is_okay = check(current_list, stack)

        # 결과 확인 : 짝을 이루면서 스택이 비어있다면 카운트 증가
        if is_okay and (not stack):
            answer += 1

    return answer