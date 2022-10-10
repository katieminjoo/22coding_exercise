# 지지난주에 못풀었던거.. 드디어 완성!
# 다시 다른 방법으로도 풀어봐야함
# for문이 너무 많고 코드가 난잡함

a = [18,26,18,24,24,20,22]
# answer [18,20,22,24,26] 5
b = [12,12,12,15,10]
# answer [12,12,12] 3
c = [4,7,1,5,3]
# answer [1,3,5,7] 4

def arithmetic(array):
    targets = sorted(array)
    answer, counts = [],[]
    # 리스트의 가장 큰 수와 가장 작은 수의 차 range 중에 하나씩 더해보며 리스트에 들어있는지 확인
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
            while idx+n <= len(targets):
                n+= 1
                if value in targets[idx+n:]:
                    values.append(value)
                    value += coin
                    count += 1
            # 한 종류의 코인을 계속 더하면서 리스트에 있는지 확인했다면 몇개를 찾았는지 append한다.
            if count > 1 :
                counts.append(count)
            if len(values) > 1:    
                answer.append(values)
    return counts, answer
    # return max(counts)

print(arithmetic(b))