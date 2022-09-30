n = int(input())
array = []
for _ in range(n):
    data = input().split()
    array.append((data[0], int(data[1])))

# key를 이용하여 정렬하기
# lambda x[1] 숫자기준 튜플 정렬
array = sorted(array, key = lambda x: x[1])

for student in array:
    print(student[0], end = ' ')