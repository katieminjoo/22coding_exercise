# Top Down (Recursion)
# Using Memoization > 한번 나온 값은 리스트에 저장해두기 때문에 또 계산되지 않는다.

# 구하려는 n 이상 만큼 리스트 초기화 (Memoization)
f = [0]*100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if f[x] != 0 :
        return f[x]
    else:
        f[x] = fibo(x-1) + fibo(x-2)
    return f[x]

print(fibo(33))