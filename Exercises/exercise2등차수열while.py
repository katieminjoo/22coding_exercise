a = [18,26,18,24,24,20,22]
# answer [18,20,22,24,26] 5
b = [12,12,12,15,10]
# answer [12,12,12] 3
c = [4,7,1,5,3]
# answer [1,3,5,7] 4

start_idx = 0
end_idx = len(a)-1
plus_num = 0
count = 0
start = a[start_idx] + plus_num

while start < max(a):
    for i in range(len(a)):
        if (a[i] + plus_num) in a[i:]:
            count += 1
            start_idx = 
            # start를 바꿔야되는데....
        else:
            plus_num += 1

