# 정수 x가 주어졌을 때 네가지 연산을 적절히 사용해서 1로 가는 연산의 최솟값 출력
# 점화식 ai = min(a(i-1), a(i/2), a(i/3), a(i/5)) + 1

x = int(input())
d = [0] * 300001

for i in range(2, x+1):
    d[i] = d[i-1] + 1
    if i%2==0:
        d[i] = min(d[i], d[i//2]+1)
    if i%3 == 0:
        d[i] = min(d[i-1], d[i//3]+1)
    if i%5 == 0:
        d[i] = min(d[i-1], d[i//5]+1)

print(d[x])