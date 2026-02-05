import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

nums = [str(input().strip()) for _ in range(N)]
visited = [False] * N
result = set()

def dfs(depth, curr):
    if depth == K:
        result.add(curr)
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, curr + nums[i])
            visited[i] = False
            
dfs(0, "")
print(len(result))