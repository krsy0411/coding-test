import sys
input = sys.stdin.readline

result = [] # 결과 출력용 리스트
inputs = [] # 입력 라인 저장용
while True:
	line = input().strip().split()
	if line == ['0']:
		break
	
	n = int(line[0]) 
	arr = list(map(int, line[1:]))
	inputs.append((n, arr)) # 튜플 형태 : (직사각형 수, n개의 높이 배열)
	
# 중간에 겹치는 영역에 대한 크기를 구하는 함수
def get_crossing_size(arr, left_idx, right_idx, mid_idx):
	max_size = arr[mid_idx]
	min_height = arr[mid_idx]
	
	l = mid_idx
	r = mid_idx
	while left_idx < l or right_idx > r:
			# 오른쪽 먼저 확장해보기(그냥)
			if r < right_idx and (l == left_idx or arr[r+1] >= arr[l-1]):
				r += 1
				min_height = min(min_height, arr[r])
			else:
				l -= 1
				min_height = min(min_height, arr[l])
			max_size = max(max_size, min_height * (r - l + 1))
	
	return max_size

# 메인 함수
def recursive_get_largest_size(arr, left_idx, right_idx):
	if left_idx > right_idx:
		return 0
	
	# 하나만 남은 경우
	if left_idx == right_idx:
		return arr[left_idx]
	
	# 마법의 요정 구간
	mid_idx = (left_idx + right_idx) // 2
	left_side_size = recursive_get_largest_size(arr, left_idx, mid_idx - 1)
	right_side_size = recursive_get_largest_size(arr, mid_idx + 1, right_idx)
	mid_crossing_size = get_crossing_size(arr, left_idx, right_idx, mid_idx)
	
	return max(left_side_size, right_side_size, mid_crossing_size)


for i in range(len(inputs)):
	n, arr = inputs[i]
	case_result = recursive_get_largest_size(arr, 0, n-1)
	result.append(case_result)
	
print('\n'.join(map(str, result)))