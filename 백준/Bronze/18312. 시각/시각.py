import sys
input = sys.stdin.readline

N, K = map(int, input().split())

hour = 0
minute = 0
second = 0

result = 0

while hour <= N:
    # 우선 K가 하나라도 포함되는 지 확인
    if str(K) in (str(int(hour / 10)), str(hour % 10)):
        result += 1
    elif str(K) in (str(int(minute / 10)), str(minute % 10)):
        result += 1
    elif str(K) in (str(int(second / 10)), str(second % 10)):
        result += 1
        
    # 초 증가
    second += 1
    if second == 60:
        second = 0
        minute += 1
    if minute == 60:
        minute = 0
        hour += 1
    
print(result)