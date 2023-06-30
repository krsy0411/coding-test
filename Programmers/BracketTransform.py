## 2020 카카오 블라인드 채용
def solution(p):
  if isCorrect(p):
    return p
  
  result = recursive(p)

  return result

def division(p):
  left,right = 0,0
  # 개폐 괄호 개수 왼쪽부터 차례대로 구함
  for i in range(len(p)):
    if p[i] == "(":
      left += 1
    else:
      right += 1

    # 만약 개폐 괄호 개수가 동일하면 -> u,v 분리
    if left == right:
      # u는 i번째까지 잘라내기
      u = p[:i+1]
      # v는 그 외 나머지 것들
      # 만약 v에 빈 문자열이 들어오면 빈 문자열로 반환
      if i+1 < len(p):
        v = p[i+1:]
      else:
        ""
      break

  return [u,v]

# 이미 division에서 개폐 괄호 개수는 맞춰서 리턴
# True -> 올바름
def isCorrect(p):
  list = []

  # 처음부터 문자열을 돌면서
  for bracket in p:
    # 만약 열린 괄호가 들어오면 담고
    if bracket == '(':
      list.append(bracket)
    # 만약 닫힌 괄호가 들어왔을때
    else:
      # 만약 리스트가 비어있으면 짝이 안 맞으므로 False반환
      if not len(list):
        return False
      # 열린 괄호가 이미 안에 존재한다면 ()짝으로 제거
      elif list[-1] == '(':
        list.pop()
      
  # 문자열을 다 돌고나서, 만약 리스트가 비어있으면 짝이 맞았단 소리이므로 True
  if len(list):
    return False
  else:
    return True

def recursive(p):
  result = ""
  # step 1 : 빈 문자열(0)이 들어오면 True -> 빈 문자열 반환
  if not len(p):
    return ""
  # step 2 : u,v 분리
  u,v = division(p)
  # step 3 : u가 올바르면 u는 그대로 붙고 v는 재귀함수 동작
  if isCorrect(u):
    result = u + recursive(v)
  # step 4 : u가 올바르지 않으면 v는 재귀적으로, u는 새로운 문자열 생성
  else:
    # 4-1
    temp = "("
    # 4-2 
    temp += recursive(v)
    # 4-3
    temp += ")"
    # 4-4
    u = u[1:-1]
    for i in u:
      if i == "(":
        temp += ")"
      else:
        temp += "("

    result += temp

  return result