# 거스름돈 n원을 최소 동전개수로 표현하기
n = 1260

coin_types = [500,100,50,10]
count = 0

for coin in coin_types:
    # 가장 큰 단위의 동전부터 거슬러주기 시작.
    # n원을 coin으로 나눈 몫을 count에 update한다.
    count += n // coin
    # 남은 금액에서 coin으로 나눈 나머지를 구하면 거슬러줄 남은 돈을 알 수 있다.
    n %= coin

# 최종적으로 거슬러줄 수 있는 최소동전의 개수
print(count)
