# 백준 13334 : 철로
import sys
import heapq
input = sys.stdin.readline

n = int(input().strip())
# 1. 입력에 대해 (집, 사무실) 두 좌표를 정렬해서 (최소, 최대) 튜플 형태로 좌표들 저장
arr = [tuple(sorted(map(int, input().strip().split()))) for _ in range(n)]
arr.sort(key=lambda x: x[1]) # 끝점을 기준으로 오름차순 정렬
d = int(input().strip())

# 2. 우선순위 큐를 사용 -> 철로에 포함된 구간들의 시작점 관리
result = 0 # 선분에 포함되는 사람들의 최대 수
pq = []
# 3. 정렬한 값에서 끝점을 기준으로 왼쪽으로 d만큼이 철로의 위치
# 4. 힙을 이용해 유효하지 않은 구간을 가진 것들은 힙에서 제거
for start, end in arr:
    # 일단 철로 길이(d)보다 넘어가는 사이즈면 무조건 탈락
    if end - start > d:
        continue
    
    # 현재 지점의 시작점을 힙에 추가
    heapq.heappush(pq, start)
    
    # 구간에 해당하지 않는 힙의 이전 최소값들을 모두 제거
    while heapq and end - pq[0] > d:
        heapq.heappop(pq)
    
    # 결과 갱신
    result = max(result, len(pq))

print(result)