import sys
input = sys.stdin.readline

A,B,C = map(int, input().strip().split())

def hyper_exp(base, n, mod_num):
	if n == 0:
		return 1
	
	half = hyper_exp(base, n // 2, mod_num)
	if n % 2 == 0:
		return (half * half) % mod_num
	else:
		return (base * half * half) % mod_num

print(hyper_exp(A,B,C))