def solution(s):
    answer = len(s)
    # 나올수있는 패턴의 최대길이인 전체 문자열 길이의 반을 뚝 자름
    for step in range(1, len(s)//2 + 1):
        # 매 압축된 패턴마다 기존 문자열, 혹은 전스텝압축문자열 의 길이보다 짧은지 확인할것
        compressed = ''
        prev = s[0:step]
        count = 1
        for j in range(step, len(s), step):
            if prev == s[j:j+step]:
                count+=1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j+step]
                count = 1
        compressed += str(count) + prev if count >=2 else prev
        answer = min(answer, len(compressed))

    return answer