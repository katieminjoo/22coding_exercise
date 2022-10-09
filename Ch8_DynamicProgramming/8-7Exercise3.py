# 점화식 세우는 것이 중요
# a(i) = a(i-1) + 2 * a(i-2)

n = int(input())

# dp 테이블 초기화
d = [0] * 1001

# DP (Bottom up)
d[1] = 1
d[2] = 3
for i in range(3, n+1):
    d[i] = (d[i-1] + 2 * d[i-2])

print(d[n])