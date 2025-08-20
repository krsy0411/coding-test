import sys
input = sys.stdin.readline

N = int(input().strip())
in_degree = [0] * (N+1) # 진입 차수

for _ in range(N-1):
    u,v = map(int, input().strip().split())
    # 무방향 그래프
    in_degree[u] += 1
    in_degree[v] += 1
    
q = int(input().strip())
for _ in range(q):
    t,k = map(int, input().strip().split())
    
    if t == 2:
        print('yes') # 단절선은 무조건 해당
    else:
        if in_degree[k] >= 2:
            # 진입차수가 2이상인 경우에만 단절점에 해당
            print('yes')
        else:
            print('no')