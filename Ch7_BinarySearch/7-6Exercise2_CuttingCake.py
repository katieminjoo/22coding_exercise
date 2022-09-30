n,m = map(int, input().split())
cakes = list(map(int, input().split()))

for i in range(0, max(cakes)):
    a_list = [cake - i for cake in cakes]
    b_list = [0 if a <= 0 else a for a in a_list]
    if sum(b_list) == m : 
        print(i)
