s = [int(i) for i in list(input())]

start = s[0]

for num in s[1:]:
    if start == 0 or start == 1:
        start += num
    else:
        if num == 0 or num == 1:
            start += num
        else:
            start *= num

print(start)