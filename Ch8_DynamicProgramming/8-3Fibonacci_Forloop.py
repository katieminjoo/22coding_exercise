# BottomUp

f = [0] * 100

f[1] = 1
f[2] = 1
n = 33

for i in range(3,34):
    f[i] = f[i-1] + f[i-2]

print(f[n])