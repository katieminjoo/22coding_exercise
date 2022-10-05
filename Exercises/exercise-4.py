a =  [18,18,20,22,24,24,26]

max_val = max(a)

data = [0] * (max_val+1)
for val in a:
    data[val] += 1
print(data)

# data table을 만들어놓고

for i in range(len(data)):
    counts = []
    if data[i] != 0 :
        start = i
        print(start)
        for plus in range(len(data) - start):
            count = 0
            if data[i+plus] != 0:
                print(data[i+plus])
                i += plus
                count += 1
            counts.append(count)

print(counts)








# 시작 위치, 최대값 3 -> (시작끝 차이) / step 가 최대값보다 작아진 순간  24 / 4 (6번)
# 특정인덱스에서 출발해서 최대값을 찾는 함수를 짜놓고
