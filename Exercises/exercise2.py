# 정렬되어있지 않은 리스트 내에서 패턴을 찾아서 가장 많은 숫자를 배출해낼 수 있는 패턴을 가진 것을 찾아야함
# 재귀로 풀어보기

# [18,18,20,22,24,24,26]
# 18부터 돌기
# count = 1
# 인덱스 0~n까지 이것을 실행
# 인덱스 [0]에 0을 더해서 [1:]에서 탐색 > 발견 count에 추가
# 0을 더하는건 그대로 두고 인덱스 범위를 발견한 인덱스[1]로 옮기기 [2:]부터 탐색
# 발견 못할 때까지 인덱스로 옮긴 다음
# count 초기화
# 다시 인덱스[0]에 1을 더하는것으로 시작

# [0]에 2를 더해 , [1:]에서 [2] 가  2 더해진 숫자라는것을 발견
# [2]에 2를 더해, [3:]에서 [3]가 2 더해진 숫자라는것을 발견
# [3]에 

a = [18,26,18,24,24,20,22]
# answer [18,20,22,24,26] 5
b = [12,12,12,15,10]
# answer [12,12,12] 3
c = [4,7,1,5,3]
# [1,3,4,5,7]
# answer [1,3,5,7] 4
# count가 몇개가 나와야되냐면 
# 1 > 0123456
# 3 > 01234
# 4 > 0123
# 5 > 012
# 7 > 0
# 총 20개


def find_pattern(array):
    counts = []
    array.sort()
    print(array)
    # 제일 작은 수부터 돌기 (현 포지션 1)
    for start_idx in range(len(array)):
        print('another start idx', start_idx)
        max_difference = max(array)-array[start_idx]
        for plus_num in range(0, max_difference+1):
            count = 1
        # 0을 더하느건 그대로 두고 찾는 인덱스를 방금 찾은 인덱스로 바꾸고 범위는 그 다음인덱스부터 찾기
            print('array_start_idx', array[start_idx])
            print('plusnum', plus_num)
            finding_num = array[start_idx] + plus_num
            print('findingnum', finding_num)
            if finding_num <= max(array):
                if finding_num in array[start_idx+1:]:
                    start_idx = array.index(finding_num)
                    count += 1
                    print('&&plusnum', plus_num)
                    print('**start_idx', start_idx)

            counts.append(count)
    return counts
            



result = find_pattern(c)
print(result)
print(len(result))


# 
# list =  [18,18,20,22,24,24,26]

max_val = max(list)

data = [0] * (max_val-1)

for val in list:
    data[val] += 1


# 시작 위치, 최대값 3 -> (시작끝 차이) / step 가 최대값보다 작아진 순간  24 / 4 
# 특정인덱스에서 출발해서 최대값을 찾는 함수를 짜놓고


