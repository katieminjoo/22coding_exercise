# 알페벳을 오름차순 정렬 이어서 출력 + 그 뒤에 모든 숫자를 더한 값 출력
s = input()
data = list(s)
count = 0
str_data = []
for i in range(len(data)):
    try:
        int(data[i])
        count += int(data[i])
    except:
        str_data.append(data[i])

str_data.sort()
final = str_data + [str(count)]
print(''.join(final))