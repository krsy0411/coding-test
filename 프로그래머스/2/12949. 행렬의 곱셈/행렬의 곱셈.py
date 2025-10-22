def solution(arr1, arr2):
    # (A,B) x (B,C) = (A,C)
    A = len(arr1) # arr1의 행
    B = len(arr1[0]) # arr1의 열
    C = len(arr2[0]) # arr2의 열
    
    # 0으로 초기화
    answer = [[0] * C for _ in range(A)]
    # 원소 계산 : (A,C) 크기의 행렬의 원소를 계산
    for i in range(A):
        for j in range(C):
            for k in range(B): # B 범위의 k값을 매개체로 사용함으로써 값 계산
                answer[i][j] += (arr1[i][k] * arr2[k][j])
    
    return answer