s = input()

# 예시 001000110001010000
# 이럴때 행동의 최소 횟수를 출력
# 붙어있는 묶음끼리 분리
# 00 1 000 11 000 1 0 1 0000
# 0 묶음, 1 묶음가 몇갠지 구분
# 0 묶음 5, 1 묶음 4 
# 더 적은 묶음 개수 출력 끝

zero_count = 0
one_count = 0

if s[-1] == '0' :
    zero_count += 1
else:
    one_count += 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i] == '0' :
            zero_count += 1
        else:
            one_count += 1

print(min(zero_count, one_count))

