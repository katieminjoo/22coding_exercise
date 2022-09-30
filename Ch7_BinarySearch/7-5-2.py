# Count Sort
# 아이템 리스트 (인덱스가 상품번호) 를 만들어놓고 존재하면 1로 값을 채우기

n = int(input())
item_list = [0] * 1000001
for i in input().split():
    item_list[int(i)] = 1
m = int(input())
m_list = list(map(int,input().split()))

for m in m_list:
    if item_list[m] == 1 :
        print('yes', end = ' ')
    else:
        print('no', end = ' ')