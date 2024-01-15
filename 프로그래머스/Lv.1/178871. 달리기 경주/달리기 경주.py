def solution(players, callings):
    dic = {player: i for i, player in enumerate(players)}
    for callingPlayer in callings:
        # 현재 불린 선수의 인덱스(순위)
        callingPlayerIndex = dic[callingPlayer]
        # 불린 선수의 추월(-1) / 추월당한 선수는 +1
        dic[callingPlayer] -= 1
        dic[players[callingPlayerIndex - 1]] += 1
        # players배열의 선수 순서 변경해주기(스와핑)
        players[callingPlayerIndex], players[callingPlayerIndex-1]  = players[callingPlayerIndex-1], players[callingPlayerIndex]
        
    return players