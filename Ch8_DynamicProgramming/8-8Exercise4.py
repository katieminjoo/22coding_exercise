# 효율적인 화폐 구성

# 나의 방식
# M원에서 거슬러줄 수 있는 가장 큰 화폐를 먼저 거슬러준다. 이를 계속 반복하다가 거슬러줄 수 없게되면 -1, 0원까지 마치면 몇번 거슬러주었는지 리턴한다.

n,m = map(int, input().split())
pocket = []
for i in range(n):
    pocket.append(int(input()))

def monetary(m):
    count = 0
    while True:
        if m == 0 :
            return count
        minus = [m-money for money in pocket if m-money >= 0]
        if not minus :
            return -1
        m = min(minus)
        count += 1

result = monetary(m)
print(result)
