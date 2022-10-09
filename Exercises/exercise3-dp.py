a = [18,26,18,24,24,20,22]
# answer [18,20,22,24,26] 5
b = [12,12,12,15,10]
# answer [12,12,12] 3
c = [4,7,1,5,3]
# answer [1,3,5,7] 4

# 점화식
# F(n) = max(F(i-coin1), F(i-coin2),...)+1

# max 를 구해야하고
# 여기서 코인수 (더하고 뺄 등차는) range(0,max(list)-min(list))

# amount 는 매번 바꾸면돼. 리스트 돌면서
# 매번 max(dp[i], dp[i-coin] +1)
# 다 업데이트를 하고 dp[amount]가 아닌 max(dp)를 구하면됨

def arithmetic(array:list[int]) -> int :
    coins = list(range(0,max(array)-min(array)+1))
    # print(coins)
    targets = array
    dp = [float('inf')] * (max(array)+1)
    dp[0] = 0
    # 18, 26
    for amount in targets:
        # 0, 8
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] =min(dp[i], dp[i-coin] +1)
    return dp
    # return max(dp) if dp[amount]!= float('inf') else -1

result = arithmetic([18,26,18,24,24,20,22])
print(len(result))
print(result)


