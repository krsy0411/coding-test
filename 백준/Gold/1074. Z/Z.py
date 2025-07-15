import sys
input = sys.stdin.readline
N,r,c = list(map(int, input().strip().split()))

def z_order(n,r,c):
    if n == 0:
        return 0
    
    if r < 2**(n-1) and c < 2**(n-1):
        # 1사분면
        return z_order(n-1, r, c) + 0
    elif r < 2**(n-1) and c >= 2**(n-1):
        # 2사분면
        return z_order(n-1, r, c - 2**(n-1)) + 2**(n-1) * 2**(n-1)
    elif r >= 2**(n-1) and c < 2**(n-1):
        # 3사분면
        return z_order(n-1, r - 2**(n-1), c) + 2**(n-1) * 2**(n-1) * 2
    else:
        # 4사분면
        return z_order(n-1, r - 2**(n-1), c - 2**(n-1)) + 2**(n-1) * 2**(n-1) * 3

# r행c열의 값
result = z_order(N, r, c)
print(result)