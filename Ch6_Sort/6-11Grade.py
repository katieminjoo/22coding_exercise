n = int(input())
array = []
for _ in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

# key를 이용하여 점수 기준 정렬
array = sorted(array, key=lambda x:x[1])

print(array)