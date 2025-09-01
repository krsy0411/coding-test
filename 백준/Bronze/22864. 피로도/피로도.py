import sys
input = sys.stdin.readline

A, B, C, M = map(int, input().strip().split())
time = 0 # 시간
tired = 0 # 피로도
result = 0 # 최대로 할 수 있는 일의 양

while time < 24:
    # 아직 일을 더 할 수 있다면(일을 해도 피로도가 M을 넘지 않는다면)
    if tired + A <= M:
        result += B
        tired += A
    else:
        tired -= C
        
        # 피로도가 음수가 되지는 못 함
        if tired < 0:
            tired = 0
            
    time += 1

print(result)