n,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# a는 오름차순 정렬, b는 내림차순 정렬
a.sort()
b.sort(reverse = True)

# 정렬을 해두면 a의 인덱스 첫번째, b의 인덱스 첫번째끼리 swap 가능
# else 사용 means it doesn't 
for i in range(k):
    if a[i] < b[i]:
            a[i],b[i] = b[i], a[i]
    else:
        break

print(sum(a))