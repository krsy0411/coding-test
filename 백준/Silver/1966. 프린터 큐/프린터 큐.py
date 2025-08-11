import sys
from collections import deque

input = sys.stdin.readline

T = int(input().strip())
while T > 0:
    N, M = map(int, input().strip().split())
    nums = deque([(i, num) for i, num in enumerate(map(int, input().strip().split()))])
    cnt_result = 0 # 문서가 몇 번째로 인쇄되는지
    
    while nums:
        idx, priority = nums.popleft()
        
        if not nums or priority >= max([p for _,p in nums]):
            cnt_result += 1
            
            if idx == M:
                print(cnt_result)
                break
        else:
            nums.append((idx, priority)) # 우선순위가 가장 높지 않다면 다시 뒤로 보내기

    T -= 1