# 백준 2261 : 가장 가까운 두 점
import sys
input = sys.stdin.readline

n = int(input().strip())
coordinates = [tuple(map(int, input().strip().split())) for _ in range(n)] # (x,y) 형태로 좌표 저장
coordinates.sort() # 좌표 오름차순 정렬

shortest_dist = float('inf') # 가장 가까운 두 점 거리(제곱 형태)

# 두 점의 거리의 제곱을 반환하는 함수
def calculate_dist_power(x1, y1, x2, y2):
    return (x2 - x1)**2 + (y2 - y1)**2

# 이분탐색하며 최소 거리의 두 점을 찾아내는 함수
def recursive_find_shortest_two_point(start, end):
    # 기저 조건을 어떻게 하지 -> 3개 이하일때?
    if (end - start) <= 2:
        min_dist = float('inf')
        for i in range(start, end):
            for j in range(i+1, end+1):
                dist = calculate_dist_power(coordinates[i][0], coordinates[i][1], coordinates[j][0], coordinates[j][1])
                if dist < min_dist:
                    min_dist = dist
        return min_dist
    
    # 분할 정복
    mid = (start + end) // 2
    # 마법의 요정이 해겷해주는 구간 : 절반씩 자르기
    left_min_dist = recursive_find_shortest_two_point(start, mid)
    right_min_dist = recursive_find_shortest_two_point(mid + 1, end)
    temp_min_dist = min(left_min_dist, right_min_dist)
    
    # 중앙선을 기준으로 temp_min_dist보다 x좌표 차이가 작은 점들만 모음
    mid_x = coordinates[mid][0]
    candidates = []
    for i in range(start, end + 1):
        if abs(coordinates[i][0] - mid_x) < temp_min_dist ** 0.5:
            candidates.append(coordinates[i])
    # y좌표 기준 정렬
    candidates.sort(key=lambda x: x[1])
    
    # y좌표 차이가 temp_min_dist보다 작은 점들만 비교
    len_candidates = len(candidates)
    for i in range(len_candidates):
        for j in range(i + 1, len_candidates):
            if (candidates[j][1] - candidates[i][1]) ** 2 >= temp_min_dist:
                break
            dist = calculate_dist_power(candidates[i][0], candidates[i][1], candidates[j][0], candidates[j][1])
            if dist < temp_min_dist:
                temp_min_dist = dist

    return temp_min_dist
    
shortest_dist = recursive_find_shortest_two_point(0,n-1)
print(shortest_dist)