import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

string_a = input().strip()
string_b = input().strip()

def get_lcs_length(a,b):
    n = len(a)
    m = len(b)
    
    dp = [[-1] * (m + 1) for _ in range(n + 1)]
    
    def lcs(i,j):
        if i == 0 or j == 0:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        
        if a[i-1] == b[j-1]:
            dp[i][j] = lcs(i-1, j-1) + 1
        else:
            dp[i][j] = max(lcs(i-1, j), lcs(i, j-1))
            
        return dp[i][j]
    
    return lcs(n,m)

lcs_length = get_lcs_length(string_a, string_b)
print(lcs_length)