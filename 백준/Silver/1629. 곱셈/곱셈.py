import sys
input = sys.stdin.readline

A,B,C = map(int, input().split())

def recursive_modular_exp(a, b, c):
    if b == 0:
        return 1

    half = recursive_modular_exp(a, b // 2, c)
    if b % 2 == 0:
        return (half * half) % c
    else:
        return (half * half * a) % c

result = recursive_modular_exp(A, B, C)
print(result)