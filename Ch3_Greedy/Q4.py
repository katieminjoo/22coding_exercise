# 만들 수 없는 동전
# 최솟값을 구하는거니까 1부터 다 만들어보기?

n = int(input())
array = list(map(int, input().split(' ')))

array.sort()

target = 1
for i in array:
    if target < i :
        break
    else :
        target += i

print(target)



