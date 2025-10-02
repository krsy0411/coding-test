import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, r, c = map(int, input().strip().split())
result = 0 # 결과 : 몇 번째로 방문했는지

def z(x,y,n):
    global result
    
    size = (2**n)
    if(size == 1): return # 기저 조건
    
    # 재귀 호출하면서 사이즈 줄여나가고 결과값 갱신
    new_size = (2**(n-1))
    if((r < (x + new_size)) and (c < (y + new_size))):
        # r,c가 1사분면에 속한 경우
        result += 0
        z(x, y, n-1)
    elif((r < (x + new_size)) and (c >= (y + new_size))):
        # r,c가 2사분면에 속한 경우
        result += (new_size**2)
        z(x, y + new_size, n-1)
    elif((r >= (x + new_size)) and (c < (y + new_size))):
        # r,c가 3사분면에 속한 경우
        result += ((new_size**2) * 2)
        z(x + new_size, y, n-1)
    else:
        # r,c가 4사분면에 속한 경우
        result += ((new_size**2) * 3)
        z(x + new_size, y + new_size, n-1)

# 함수 실행 & 결과 출력
z(0,0,N)
sys.stdout.write(str(result))