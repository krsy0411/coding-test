import sys
input = sys.stdin.readline

n,m = map(int, input().strip().split())

# C(n,r) = n! / (r! × (n-r)!)
def factorial(n):
    if n <= 1:
        return n
    
    return factorial(n-1) * n

result = factorial(n) // (factorial(m) * factorial(n-m))
print(result)