import sys
input = sys.stdin.readline

S = int(input().strip())
N = 0 # N의 값 : 서로 다른 자연수들의 개수

while S > 0:
    N += 1
    S -= N
    
    if S < 0:
        N -= 1
        break

print(N)