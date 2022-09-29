# Insertion sort 삽입정렬
# 데이터가 거의 정렬되어있을 때 훨씬 효율적
# 첫번째 원소는 그대로 두고 두번째 원소부터 첫번째보다 큰지 작은지 비교하여 삽입한다.
# 계속해서 뒤로 가면서 원소 하나를 앞 원소들 보다 큰지 작은지 하나씩 확인하여 삽입한다.
# O(N)^2

array = [7,5,9,0,3,1,6,2,4,8]

# 두번째 원소부터 확인 (i : 비교대상)
for i in range(1, len(array)):
    # i번째부터 0번째 인덱스까지 거꾸로 가며 i번째원소와 비교하기
    for j in range(i,0,-1):
        if array[j-1] > array[j]:
            # 앞원소와 비교하여 본인이 더 작으면 순서를 바꾸기
            array[j],array[j-1] = array[j-1],array[j]
        else:
            # 앞원소와 비교하여 본인이 더 크면 그대로 있기
            break

print(array)


