# 풀이방법 2
# 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는데, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없음
# 배열의 크기 N, 숫자가 더해지는 횟수 M, K번까지 연속해서 더해질수있음

n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))

# numbers를 정렬하기
numbers.sort()
first = numbers[n-1] # 가장 큰 수 
second = numbers[n-2] # 두번째로 큰 수

# 항상 (가장큰수 * K번 + 두번째큰수 * 1), 즉, k+1 이 반복된다.
# # 그래서 m에서 k+1을 나눈 몫만큼 저 식을 반복해주고 나머지만큼 가장큰수를 더해준다.
# 첫번째 방법

answer = ((m // (k+1)) * (first*k + second)) + ((m % (k+1)) * first)
print(answer)

# 2번째 방법가장 큰 수가 더해지는 횟수 구하기
count = (m // (k+1)) * k
count += (m % (k+1))

result = 0
result += count * first
result += (m-count) * second

print(result)
