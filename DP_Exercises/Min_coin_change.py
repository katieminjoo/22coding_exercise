# Leetcode 322
# https://leetcode.com/problems/coin-change/
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.

# 최소 갯수 동전 바꾸기 : 주어진 동전 coins로 금액의 합 amount를 만들기 위한 최소한의 동전의 갯수는 몇개인가?
# 정수 x가 주어졌을 때 네가지 연산을 적절히 사용해서 1로 가는 연산의 최솟값 출력 (8-5.py랑 굉장히 유사)
# 8-8.py와 같은 문제!

# coins=[2,3,5]
# amount = 10
# 일 때 10에서 2를 뺀 값, 3을 뺀 값, 5를 뺀 값을 구하고 0이 될때까지 쭉... 
# array에는 거기까지 도달한 총 연산횟수가 저장되어있고 coins를 뺀 경우의 수 중 가장 적은 연산횟수가 저장된 array를 선택해서 거기에서 +1 을 하면 다음 연산이 됨

# 1. 점화식을 세움
# +1 means 1 more coin
# F(n) = min(F(i-2), F(i-3), F(i-5)) + 1

def coinChange(coins: list[int], amount: int) -> int:
    dp = [float('inf')] * (amount+1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount+1) :
            # 이전 코인으로 만들어진 조합 vs 현재 쌓고 있는 코인으로 만든 조합
            dp[i] = min(dp[i], dp[i-coin] + 1)
    return dp[amount] if dp[amount]!= float('inf') else -1

print(coinChange([2,3,5], 10))
