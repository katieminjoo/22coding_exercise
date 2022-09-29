# 현재 위치 입력받기
n = input()
str_x = n[0]
y = int(n[1])

# alphabet to number
alphabet_list = ['a','b','c','d','e','f','g','h']
for i, alphabet in enumerate(alphabet_list,1):
    if str_x == alphabet:
        x = i

# 이동 시도 및 계산
count = 0
moves = [(2,1),(2,-1),(-2,1),(-2,-1), (1,2),(-1,2),(1,-2),(-1,-2)]
for m in moves:
    next_x = x + m[0]
    next_y = y + m[1]
    if next_x >=1 and next_x <= 8 and next_y >= 1 and next_y <= 8 :
        count+=1
print(count)



