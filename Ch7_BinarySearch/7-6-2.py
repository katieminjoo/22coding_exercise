# Binary Search and Parametric Search
# 원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제

# 절단기의 높이는 1부터 10억까지의 정수 중 하나이므로 이진 탐색

# 시작점은 0, 끝점은 가장 긴 떡의 길이.
# 중간점 으로 절단기 높이를 설정하면 얻을 수 있는 떡의 길이의 합은 ~.. 필요한 떡보다 기니까 더 잘라야함. 절단기를 더 높이 올려야함.(오른쪽 탐색) 시작점을 증가시킴.
# 필요한 떡보다 짧은 경우 절단기를 더 낮추어야하니 끝점을 내리기.(왼쪽 탐색)

n,m = map(int, input().split())
cakes = list(map(int, input().split()))
start = 0
end = max(cakes)

result = 0
while start <= end :
    total = 0
    mid = (start+end)//2
    for x in cakes:
        if x > mid :
            total += x-mid
    # 총 잘린 떡이 필요한 떡보다 짧을 때 -> 떡이 더 필요하니 절단기를 낮추기 (왼쪽 부분 탐색)
    if total < m :
        end = mid-1
    # 총 잘린 떡이 필요한 떡보다 길 때 -> 떡이 덜 필요하니 절단기를 높여서 오른쪽 부분 탐색
    else:
        result = mid
        start = mid + 1

print(result)