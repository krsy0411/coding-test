def solution(want, number, discount):
    answer = 0
    N = len(discount)
    window_size = 10
    
    want_data = {}
    for i in range(len(want)):
        w = want[i]
        n = number[i]
        want_data[w] = n
        
    for i in range(N - window_size + 1):
        is_possible = True
        temp_data = want_data.copy()
        
        for j in range(i, i + window_size):
            discounted_name = discount[j]

            if discounted_name in temp_data:
                temp_data[discounted_name] -= 1
                
        for n in temp_data.values():
            if n > 0:
                is_possible = False
                break

        if is_possible:
            answer += 1
    
    return answer