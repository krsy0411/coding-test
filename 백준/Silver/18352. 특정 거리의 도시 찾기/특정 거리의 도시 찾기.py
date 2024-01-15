from collections import deque

#  4개의 도시, 4개의 도로, 거리 정보 2, 출발 도시 번호 1
n, m, k, x = map(int, input().split())

# 각 도시들에 대한 정보 : 각 도시마다 어떤 도시로 갈 수 있는지 담는 배열 : (0),1,......,n번 도시
graph = [[] for _ in range(n+1)]
# 모든 도시들에 대한 최단거리 정보 : (0), 1,.....,n번 도시
shortDistance = [-1]*(n+1)
# 출발 도시에서 출발 도시까지의 거리는 0
shortDistance[x] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# x번 도시에서 출발
q = deque([x])
while q:
    currentCity = q.popleft()
    # 현재 도시 인근의 도시들 탐색
    for nextCity in graph[currentCity]:
        # 아직 최단거리 정보가 -1이면 : 즉, 아직 방문하지 않았다면
        if shortDistance[nextCity] == -1:
            # 현재까지의 거리 + 1 한게 다음 도시까지의 거리
            shortDistance[nextCity] = shortDistance[currentCity] + 1
            q.append(nextCity)

isValid = False
# 1번 도시부터 n번 도시까지
for i in range(1, n+1):
    # 거리 정보와 최단거리 값이 동일하면 해당 도시 번호 오름차순 출력
    if shortDistance[i] == k:
        print(i)
        isValid = True

# 만약 일치하는 최단거리 값이 없다면?
if (isValid == False):
    print(-1)
