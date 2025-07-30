import sys
input = sys.stdin.readline

N = int(input().strip())
A = [0] + list(input().strip())
result = 0 # 가능한 서로 다른 산책 경로의 수

graph = [[] for _ in range(N + 1)]
for _ in range(N-1):
	u,v = map(int, input().strip().split())
	# 무방향 그래프
	graph[u].append(v)
	graph[v].append(u)
	
	# (실내 - 실내) 산책 경로
	if A[u] == 1 and A[v] == 1:
		result += 2

def dfs(node, visited):
	count = 0 # 실내 노드의 개수
	
	visited[node] = True
	for neighbor in graph[node]:
		if A[neighbor] == 1:
			count += 1
		elif not visited[neighbor]:
			# 방문한 적 없는 실외가 인접노드인 경우
			count += dfs(neighbor, visited)

	return count

# 실외가 포함된 산책 경로
indoor_count = 0
visited = [False] * (N + 1)
for start in range(1, N+1):
	if A[start] == 0 and not visited[start]:
		# 실외와 인접한 실내 노드를 찾기
		indoor_count += dfs(start, visited)

result += ((indoor_count) * (indoor_count - 1))
print(result)