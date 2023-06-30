import sys
# 입력
n = int(input())
n_data_list = list(map(int, input().split()))

m = int(input())
m_data_list = list(map(int, input().split()))
# 이진 탐색을 위해서는 정렬 필요
m_data_list.sort()

# 이진 탐색 함수
def binary_serach(arr, target, start, end):
  # 만약 시작 인덱스가 끝보다 더 크면 종료
  if start > end :
    return None
  # 중간값 인덱스 설정
  middle = (start + end) // 2
  # 만약 중간값과 타겟값이 일치하면
  if arr[middle] == target:
    return middle
  # 만약 중간값보다 타겟이 작으면 중간값 왼쪽값들만 재귀
  elif arr[middle] > target:
    return binary_serach(arr, target, start, arr[middle] - 1)
  # 중간값보다 타겟이 큰 경우 오른쪽값들만 재귀
  else:
    return binary_serach(arr, target, arr[middle] + 1, end)


# 결과 출력 : 찾아야하는 부품이 여러 개 이므로 반복문 이용
for i in m_data_list:
  result = binary_serach(m_data_list, i, 0, n-1)
  if result != None:
    print('yes', end=' ')
  else:
    print('no', end=' ')