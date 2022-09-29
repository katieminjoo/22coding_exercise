# 선택정렬
# 첫번째 인덱스 원소와 그 뒤의 원소들을 비교하여 가장 작은 데이터를 앞으로 보내는 과정을 n-1번 반복
# O(N)^2


array = [7,5,9,0,3,1,6,2,4,8]

# 뒤의 원소들과 비교할 원소 i
for i in range(len(array)):
    min_idx = i
    # 뒤의 원소들 j
    for j in range(i+1, len(array)):
        if array[min_idx] > array[j] :
            min_idx = j
    array[i], array[min_idx] = array[min_idx], array[i]

print(array)
