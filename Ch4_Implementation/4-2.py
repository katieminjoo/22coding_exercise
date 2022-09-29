# # 00 00 00 ~ 23 59 59
# # 24 * 60 * 60 의 경우의수

# n = int(input())

# # hour (00~n)
# hour = 0
# for h in range(n+1):
#     if '3' in str(h):
#         hour += 1

# minute,second = 0,0
# for m in range(60):
#     if '3' in str(m):
#         minute += 1
#         second += 1
# print(minute,second)

# print(hour * minute * second)

n = int(input())

count = 0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h)+str(m)+str(s):
                count += 1
print(count)