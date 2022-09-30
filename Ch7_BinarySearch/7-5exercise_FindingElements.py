# 부품찾기 by BinarySearch
# start index and end index
def binarysearch(array, target, start, end):
    while start <= end :
        mid = (start+end)//2
        if target == array[mid]:
            return mid
        elif target < array[mid] :
            end = mid-1
        else:
            start = mid+1
    return None

n = int(input())
n_list = input().split()
# sort
n_list.sort()
m = int(input())
m_list = input().split()

for i in m_list:
    result = binarysearch(n_list, i, 0, n-1)
    if result == None :
        print('no', end = ' ')
    else:
        print('yes', end = ' ')



