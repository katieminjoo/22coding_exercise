# while문 사용 풀이
# 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는데, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없음
# 배열의 크기 N, 숫자가 더해지는 횟수 M, K번까지 연속해서 더해질수있음

n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))

# numbers를 정렬하기
numbers.sort()
first = numbers[n-1] # 가장 큰 수 
second = numbers[n-2] # 두번째로 큰 수
result = 0
# 총 m번을 더하는데 한숫자당 k번까지 더해질 수 있음
while True :
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)