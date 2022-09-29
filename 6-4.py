# 퀵정렬 Quick sort
# 피봇을 기준으로 피봇보다 작은 것, 큰것으로 양옆으로 나누고, 또 그 리스트에서 피봇을 정하고 나누고 반복 - 재귀함수 사용
# 시간 복잡도 O(NlogN)

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x < pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))