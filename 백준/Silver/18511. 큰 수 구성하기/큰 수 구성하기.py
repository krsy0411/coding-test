import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))

result = 0

# 함수 정의
def dfs(cur):
    global result
    
    if cur > N:
        return
    
    result = max(cur, result)
    for next in nums:
        dfs(cur*10 + next)
    
# 함수 실행
dfs(0)
# 결과 출력
print(result)