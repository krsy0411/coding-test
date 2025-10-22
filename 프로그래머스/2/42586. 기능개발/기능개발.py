from collections import deque
import math

MAX_PERCENT = 100
def solution(progresses, speeds):
    answer = []
    needed_days = []
    for p, s in zip(progresses, speeds):
        needed_days.append(math.ceil((MAX_PERCENT - p) / s))
        
    q = deque(needed_days)
    while q:
        max_day = q.popleft()
        current_count = 1
        
        while q:
            next_day = q[0]
            
            if next_day <= max_day:
                q.popleft()
                current_count += 1
            else:
                break
    
        answer.append(current_count)
    
    return answer