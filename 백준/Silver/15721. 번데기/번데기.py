import sys
input = sys.stdin.readline

A = int(input().strip())
T = int(input().strip())
target = int(input().strip())

total_target_cnt = 0 # 현재까지 target을 외친 횟수
current_shout_idx = 0 # 현재 인덱스
n = 2

while True:
    # 1. "뻔-데기-뻔-데기" 시작 부분 처리
    for shout in [0,1,0,1]:
        if shout == target:
            total_target_cnt += 1
            
            if total_target_cnt == T:
                print(current_shout_idx % A)
                sys.exit()
        current_shout_idx += 1
    # 2. "뻔" n번 반복 처리
    for _ in range(n):
        if target == 0:
            total_target_cnt += 1
            
            if total_target_cnt == T:
                print(current_shout_idx % A)
                sys.exit()
        current_shout_idx += 1
    # 3. "데기" n번 반복 처리
    for _ in range(n):
        if target == 1:
            total_target_cnt += 1
            
            if total_target_cnt == T:
                print(current_shout_idx % A)
                sys.exit()
        current_shout_idx += 1
    # 한 회차 다 돌았으니 1 증가
    n += 1