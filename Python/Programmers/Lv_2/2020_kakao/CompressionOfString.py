## 2020 카카오 블라인드 채용

def solution(s):
  result = len(s)
  # 절반 개수만큼은 잘라내도 ok
  for lenOfParsing in range(1,len(s)//2 + 1):
    # 문자열 조합 잘라냄
    parcedString = s[0:lenOfParsing]
    count = 1
    # 현재 압축된 버전
    compressed_s = ''

    # 다음 문자열이 일치하는 지 확인
    for j in range(lenOfParsing, len(s), lenOfParsing):
      # 만약 다음 문자열 조합이 이전 값과 일치하면 카운트 + 1
      if parcedString == s[j:j+lenOfParsing]:
        count += 1
      # 만약 더이상 조합이 일치하지 않는다면
      else:
        # 겹치는게 2개 이상이여야 숫자로 압축
        if count >= 2:
          compressed_s += str(count) + parcedString
        # 2개 이상 겹치는게 아니면 그대로 파싱
        else:
          compressed_s += parcedString
        # 카운트 초기화
        count = 1
        # 문자열 조합 초기화
        parcedString = s[j:j+lenOfParsing]
    
    # 남아 있는 문자열 처리
    if count >= 2:
      compressed_s += str(count) + parcedString
    else:
      compressed_s += parcedString
    # 매 단계마다 가장 작은 문자열 개수인 경우를 결과로 업데이트
    result = min(result, len(compressed_s))
  return result