def solution(s):
    answer = len(s)
    # 압축 최적화 > 총 문자열이 제일 짧을 때
    # 문자열은 앞에서부터 잘라야하기때문에 맨 앞문자가 다시 한번 나오면 cut.
    for step in range(1, len(s)//2 + 1):
        # i부터 len(s)//2 까지 chunk를 확인
        compressed = ''
        # 패턴이라고 가정하고 추출
        prev = s[0:step]
        # 첫번째 패턴 발견
        count = 1
        # step 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 같은 패턴을 한번 더 찾았다면 += 1
            if prev == s[j:j+step]:
                count += 1
            # 다른 패턴이 나왔다면
            else:
                # 지금까지 2번이상 나온 패턴이 있으면 숫자+문자열 압축해서 저장, 아니면 그냥 raw 상태로 저장
                compressed += str(count) + prev if count >= 2 else prev
                # 상태 초기화 ( 저장한 것 다음부터 다시 확인)
                prev = s[j:j+step]
                # 카운트 초기화
                count = 1
        # 남아있는 문자열 처리
        # 마지막에 else로 가지못하고 if문에서 끝났을때
        compressed += str(count) + prev if count >= 2 else prev
        # 만들어진 압축 문자열이 가장 짧은 것이 정답 (매 스텝마다 비교)
        answer = min(answer, len(compressed))
    
    return answer