a = [18,26,18,24,24,20,22]
# answer [18,20,22,24,26] 5
b = [12,12,12,15,10]
# answer [12,12,12] 3
c = [4,7,1,5,3]
# answer [1,3,5,7] 4

def arithmetic(array):
    targets = sorted(array)
    answer = []
    counts = []
    coins = list(range(0, max(targets)-min(targets)+1))
    # target 먼저 돌아가기
    for idx in range(len(targets)):
        # 코인 한개씩 돌아가기
        for coin in coins:
            n = 0
            count = 1
            values = []
            values.append(targets[idx])
            value = targets[idx] + coin
            while idx+n < len(targets):
                n+= 1
                if value in targets[idx+n:]:
                    values.append(value)
                    value += coin
                    count += 1
            counts.append(count)
            answer.append(values)
    # return counts, answer
    return max(counts)

print(arithmetic(b))