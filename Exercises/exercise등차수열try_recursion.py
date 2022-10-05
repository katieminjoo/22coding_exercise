a = [18,26,18,24,24,20,22]
# answer [18,20,22,24,26] 5
b = [12,12,12,15,10]
# answer [12,12,12] 3
c = [4,7,1,5,3]
# answer [1,3,5,7] 4

print(sorted(a))
print(sorted(b))
print(sorted(c))

def finding(array, plus_num, start_idx, end_idx, count):
    array.sort()
    count_list = []
    # while plus_num <= (array[end_idx]- array[start_idx]):
    # 리스트 내 숫자를 하나씩 돈다.
    for i in range(len(array)):
        if plus_num <= (array[-1]-array[0]):
            if array[i] + plus_num in array[i:]:
                count += 1
                finding(array[i+1:], plus_num, start_idx+1, end_idx, count)
                print('count+1')
                print(count)
            else:
                print('else로')
                count_list.append(count)
                count = 0
                plus_num += 1
    return count_list




result = finding(a, 0, 0, len(a), 0)
print(result)