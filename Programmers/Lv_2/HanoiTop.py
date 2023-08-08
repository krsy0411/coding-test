# 하노이의 탑
# 입력: 옮기려는 원반의 갯수 n
#      옮길 원반이 현재 있는 출발점 기둥 from_pos
#      원반을 옮길 도착점 기둥 to_pos
#      옮기는 과정에서 사용할 보조 기둥 other_pos
# 출력: 원반을 옮기는 순서

# 시간 끌린 이유 : 3개의 기둥만 생각하면 되는데, 혹시 다른 기둥이 더 있으면 어떤 식으로 해결해야하나...하는 멍청한 생각함

def hanoi(n, from_pos, to_pos, other_pos):
    if n == 1:  # 원반 한 개를 옮기는 문제면 그냥 옮기면 됨
        print(from_pos, "->", to_pos)
        return

    # 원반 n - 1개를 other_pos로 이동(to_pos를 보조 기둥으로)
    hanoi(n - 1, from_pos, other_pos, to_pos)
    # 가장 큰 원반을 목적지로 이동
    print(from_pos, "->", to_pos)
    # other_pos에 있는 원반 n-1개를 목적지로 이동(from_pos를 보조 기둥으로)
    hanoi(n - 1, other_pos, to_pos, from_pos)
