import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())
arr = [0] + [int(input()) for _ in range(N)]

visited = [False] * (N + 1)
finished = [False] * (N + 1)
result = []

def dfs(num, path):
    visited[num] = True
    path.append(num)
    next_num = arr[num]

    if not visited[next_num]:
        dfs(next_num, path)
    elif next_num in path:
        idx = path.index(next_num)
        result.extend(path[idx:])

    finished[num] = True
    return

for i in range(1, N + 1):
    if not visited[i]:
        dfs(i, [])

result.sort()
print(len(result))
sys.stdout.write('\n'.join(map(str, result)) + '\n')