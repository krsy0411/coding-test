import sys
input = sys.stdin.readline

N = int(input().strip())
result = 0

if(N <= 99):
    result = N
else:
    result = 99

    for n in range(100, N+1):
        string_n = str(n)
        term = int(string_n[0]) - int(string_n[1])
        is_ok = True # 숫자가 한수인지 여부
    
        for i in range(len(string_n)-1):
            # 각 자리수의 차이 계산
            temp_term = int(string_n[i]) - int(string_n[i+1])
        
            # 등차가 아닌 경우
            if(term != temp_term):
                is_ok = False
                break
        
        if is_ok:
            result += 1

print(result)