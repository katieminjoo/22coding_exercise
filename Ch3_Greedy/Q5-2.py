n,m = map(int, input().split())
data = list(map(int, input().split()))

#1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m+1):
    n -= array[i]
    result += array[i] * n

print(result)

