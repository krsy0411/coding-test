## 2020 카카오 블라인드 채용

# 빈 문자열 -> 빈 문자열 반환
# w -> u,v
# u == 올바른 괄호 문자열 -> v에 대해 1단계부터

data = ["(()())()", ")(", "()))((()"]

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
      if p[i+1:] == "":
        v = ""
      else:
        v = p[i+1:]

  return [u,v]

# 이미 division에서 개폐 괄호 개수는 맞춰서 리턴
# 분리된 문자열이 True면 올바름, False라면 균형잡힘
def isCorrect(p):
  open, close = "(", ")"
  result = True

  # 만약 맨 처음이 닫히는 구조면
  if p[0] == close:
    # 올바르지 않음
    result = False
  # 처음이 열리는 구조라면 올바름 
  return result


def solution(p):
  result = ""
  [u,v] = division(p)

  # u가 올바르다 -> v를 다시 재귀 수행
  if isCorrect(u) == True:
    division(v)
  # u가 균형잡혔다 -> v는 다시 재귀 수행, u는 4단계 수행
  else:
    division(v)
  