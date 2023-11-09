from collections import deque


def solution(players, callings):
    # 문제점 : callings(100만개)를 탐색
    for call in callings:
        # call과 일치하는 player를 최대 5만의 players에서 탐색
        # 즉, 100만 X 5만 = 500만번 -> 시간 초과
        currentCallingPlayerIndex = players.index(call)

        players[currentCallingPlayerIndex], players[currentCallingPlayerIndex -
                                                    1] = players[currentCallingPlayerIndex-1], players[currentCallingPlayerIndex]

    return players


# players 문자열 배열, callings는 해당 선수
# callings에서 불린 선수가 등수 하나를 추월 : 문자열 배열


def solution(players, callings):
    answer = []
    q = deque(callings)
    while q:
        currentCallingPlayer = q.popleft()
        # 추월하기
        for i in range(len(players)):
            # 만약 추월한 선수 이름을 players에서 찾아내면
            if players[i] == currentCallingPlayer:
                # 스워핑
                players[i-1], players[i] = players[i], players[i-1]

    for player in players:
        answer.append(player)

    return answer


################################################################

# 이게 올바른 풀이

def solution(players, callings):
    dic = {player: i for i, player in enumerate(players)}
    for callingPlayer in callings:
        # 현재 불린 선수의 인덱스(순위)
        callPIdx = dic[callingPlayer]
        # 불린 선수의 추월(-1) / 추월당한 선수는 +1
        dic[callingPlayer] -= 1
        dic[players[callPIdx - 1]] += 1
        # players배열의 선수 순서 변경해주기(스와핑)
        players[callPIdx], players[callPIdx -
                                   1] = players[callPIdx-1], players[callPIdx]

    return players
