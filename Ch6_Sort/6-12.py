n,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# k번의 바꿔치기를 통해 a의 합을 젤 크게 만들어서 합을 출력
# a에서 젤 작은 수를 b의 젤 큰 수랑 바꾸면됨 (k번 수행)

for _ in range(k):
    min_a_idx = a.index(min(a))
    max_b_idx = b.index(max(b))
    a[min_a_idx], b[max_b_idx] = b[max_b_idx],a[min_a_idx]

print(sum(a))
    
