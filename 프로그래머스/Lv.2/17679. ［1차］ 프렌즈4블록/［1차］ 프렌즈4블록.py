def check(m, n, board):
    # 보드크기의 map변수 생성
    map = [[0 for _ in range(n)] for _ in range(m)]
    count = 0

    # 1. 제거 가능한 블록들 확인
    ## 만약 제거 가능한 묶음 발견하면 1로 변환
    for i in range(m-1):
        for j in range(n-1):
            a = board[i][j]
            b = board[i][j+1]
            c = board[i+1][j]
            d = board[i+1][j+1]
            if a == b == c == d and a != '0':
                map[i][j], map[i][j+1], map[i+1][j], map[i+1][j+1] = 1, 1, 1, 1

    # 2. 제거 가능한 블록들은 카운팅하면서 0으로 전환
    for i in range(m):
        for j in range(n):
            if map[i][j] == 1:
                count += 1
                board[i][j] = '0'

    # 3. 만약 제거 가능한 블록이 없으면 0출력
    if count == 0:
        return 0

    # 4. 제거되고 위에 붕 뜬 블록들 밑으로 내리기
    for i in range(m-2, -1, -1):
        for j in range(n):
            # 비교하기 위한  행 인덱스
            temp_i = i
            # 만약 map크기 내에서 동일 열에서 행을 하나씩 내릴때 0이 있으면 행 인덱스를 계속 내린다
            while 0 <= temp_i+1 < m and board[temp_i+1][j] == '0':
                temp_i += 1
            # 만약 행을 내릴 수 있어서 temp_i가 원래 인덱스와 값이 다르면 값 스위칭
            if temp_i != i:
                board[temp_i][j] = board[i][j]
                board[i][j] = '0'

    return count


def solution(m, n, board):
    answer = 0
    board = list(map(list, board))

    while True:
        temp = check(m, n, board)
        if temp == 0:
            break
        answer += temp

    return answer
