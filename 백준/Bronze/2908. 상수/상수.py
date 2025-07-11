import sys
input = sys.stdin.readline

A,B = list(map(int, input().strip().split()));
reversed_A = int(str(A)[::-1])
reversed_B = int(str(B)[::-1])

sys.stdout.write(str(reversed_A) if reversed_A > reversed_B else str(reversed_B) + '\n')