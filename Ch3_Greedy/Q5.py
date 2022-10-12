# n개의 볼링공, 최대 무게 m, 볼링공무게 리스트 K
n,m = map(int, input().split(' '))
k = list(map(int,input().split(' ')))
k.sort()
count = 0

for i in range(len(k)):
    for j in range((i+1),len(k)):
        if k[i] != k[j]:
            count += 1

print(count)