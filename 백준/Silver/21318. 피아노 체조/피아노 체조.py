import sys

input = sys.stdin.readline
N = int(input().strip()) # 악보 개수
notes_level = list(map(int, input().strip().split())) # 각 악보의 난이도

accumulated_failures = [0] * (N + 1) # 누적 실패 횟수 저장용 배열
for i in range(1, N):
    # 현재 악보 난이도가 이전 악보 난이도보다 낮으면 실패 횟수 1 증가
    if notes_level[i] < notes_level[i - 1]:
        accumulated_failures[i + 1] = accumulated_failures[i] + 1
    else:
        accumulated_failures[i + 1] = accumulated_failures[i]

M = int(input().strip()) # 질문(쿼리) 개수
for _ in range(M):
    L, R = map(int, input().strip().split()) # L: 시작 악보, R: 끝 악보
    fail_counts = accumulated_failures[R] - accumulated_failures[L] # 정답 출력용 변수 : 실패한 횟수

    print(fail_counts)