
# n=화폐가짓수, m=금액
n,m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

# 한번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m+1)

# DP 진행
#0원을 만들 수 있는 것은 없음
d[0] = 0

# 화폐가짓수 중
for i in range(n):
    # 현재 화폐 단위부터 그 이상의 금액까지 중 (화폐 단위보다 더 작은 돈은 만들지 못함)
    for j in range(array[i], m+1):
        # 금액 - 현재화폐단위 != 10001 (만들 수 있는 방법이 존재하는 경우)
        if d[ j - array[i] ] != 10001:
            # 현재금액을 만들 수 있는 방법 (이미 다른 화폐단위로 만들 수 있어서 쌓여있던 값) vs 현재금액-화폐단위를 뺐을 경우 +1 둘중에 더 적은 값을 반환
            d[j] = min(d[j], d[j-array[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001:
    print(-1)
else:
    print(d[m])

