# 큰 수부터 작은 수의 순서로 정렬하는 프로그램

n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

array = sorted(array, reverse = True)

for x in array:
    print(x, end = ' ')
