import sys
input = sys.stdin.readline

N = int(input())
result = 0 # 결과 : 경우의 수
row = [0] * N # [i,j] == (row[i] = j)

def position_ok(x):
    for i in range(x):
        if row[i] == row[x] or abs(x-i) == abs(row[x] - row[i]):
            return False
    return True

def n_queens(x):
    global result
    
    if x == N:
        result += 1
        return
    else:
        for i in range(N): # x행의 모든 열에 대해 검사
            row[x] = i # x행 i열
            
            if position_ok(x):
                n_queens(x+1) # 다음 진행
                
# 결과 확인
n_queens(0)
sys.stdout.write(str(result) + '\n')