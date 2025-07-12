import sys
input = sys.stdin.readline

N = int(input())
result = []

# 재귀함수
def hanoi(n, start, end, temp):
    if n == 1:
        sys.stdout.write(f"{start} {end}\n")
        return
    
    hanoi(n-1, start, temp, end)
    sys.stdout.write(f"{start} {end}\n")
    hanoi(n-1, temp, end, start)
    
sys.stdout.write(str(2**N - 1)+ '\n') # 이동횟수는 계산 가능
if N <= 20:
    hanoi(N, 1, 3, 2) # 함수 실행 -> 이동과정도 출력