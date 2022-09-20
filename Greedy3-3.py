# 숫자카드게임
# n*m 형태의 카드들이 주어지고 행의 카드들 중에 가장 낮은 카드를 뽑아야하는데 최종결과로는 가장 높은 숫자의 카드를 뽑을 수 있도록 전략세우기

n,m = map(int, input().split())
result=0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)