# 정렬이 되어있을 때 사용가능
# 시간복잡도 O(logN)
def recursive_binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif target < array[mid]:
        return recursive_binary_search(array, target, start, mid-1)
    else:
        return recursive_binary_search(array, target, mid+1, end)

def for_binary_search(array, target, start, end):
    while start <= end :
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif target < array[mid]:
            end = mid-1
        else:
            start = mid+1
    return None 
    
# 원소의개수(n)과 찾고자 하는 문자열(target)을 입력받기
n,target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = recursive_binary_search(array, target, 0, n-1)
if result == None :
    print('원소가 존재하지 않습니다.')
else:
    print(result+1)

result = for_binary_search(array, target, 0, n-1)
if result == None :
    print('원소가 존재하지 않습니다.')
else:
    print(result+1)