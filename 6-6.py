# 계수정렬 Count Sort

# 모든 원소의 값이 0보다 크거나 같을때
array =[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

# 최소 숫자부터 최대숫자까지 범위의 리스트 선언 (모든 값은 0으로 초기화)
count = [0] * (max(array)+1)
print(count)

for i in range(len(array)):
    count[array[i]] += 1

print(count)

for i in range(len(count)):
    # i를 출력
    for j in range(count[i]):
        print(i, end = ' ')