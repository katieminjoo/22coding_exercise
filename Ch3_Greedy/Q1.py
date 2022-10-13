# 모험가길드
# 1 2 2 2 3

n = int(input())
array = list(map(int, input().split(' ')))
array.sort()

result = 0
count = 0

for i in array :
    count += 1
    if count >= i :
        result += 1
        count = 0

print(result)