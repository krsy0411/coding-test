import sys
input = sys.stdin.readline

T = int(input().strip())
MAX = 10000

def get_primes():
    is_primes = [True] * (MAX+1);
    is_primes[0] = False
    is_primes[1] = False
    
    for i in range(2, int(MAX**0.5)+1):
        if is_primes[i]:
            for j in range(i*i, MAX+1, i):
                is_primes[j] = False
                
    return is_primes

is_primes = get_primes()
for _ in range(T):
    N = int(input().strip())
    
    for i in range(N//2, 1, -1):
        if is_primes[i] and is_primes[N-i]:
            sys.stdout.write(f"{i} {N-i}" + '\n')
            break