'''
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''
# 방법(경우의 수)이 몇개가 있는지 생각하기 (어떤 방법인지보다)
# 한개의 계단까지 올라가는데 방법 1가지 (1칸)
# 두개의 계단까지 올라가는데 방법 2가지 (1칸, 2칸)

def climb(top):
    dp = [0] * (top+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, top+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[top]

print(climb(7))