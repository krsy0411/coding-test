def solution(n, left, right):
    answer = []
    
    for i in range(left, right + 1):
        row = i // n # 행 == 몫
        col = i % n # 열 == 나머지
        
        val = max(row, col) + 1
        answer.append(val)
    
    return answer