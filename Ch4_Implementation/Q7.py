# 현재 캐릭터의 점수 N
# 자릿수기준 점수 N을 반으로 나누어 왼쪽 부분 자릿수합 == 오른쪽 부분 각 자릿수 합

n = input()
idx = int(len(n)/2)

a = sum(list(map(int,list(n[:idx]))))
b = sum(list(map(int,list(n[idx:]))))

if a == b:
    print('lucky')
else:
    print('ready')
